#!/usr/bin/env python3
"""
Equinet — deployed token diff.

    python tools/check-deployed-tokens.py path/to/deployed/tokens.css

Compares the `/modules/tokens.css` that HubSpot actually serves against this
repo's `tokens.css`, which is the source of truth for names and values.

WHY THIS IS NEEDED, AND WHY NOTHING ELSE CATCHES IT
    Modules read every value as `var(--equinet-…, <fallback>)`. That fallback
    is deliberate — README: "If the token file is ever unreachable the module
    still renders at its exact intended value." The consequence is that a
    module whose token is MISSING from the deployed file renders perfectly
    anyway, on the fallback. Drift between these two files is therefore
    invisible on every page you can look at. You only discover it when you
    change a token value, expect the modules to follow, and nothing moves —
    because they were never reading the token.

FOUR BUCKETS, AND ONLY TWO OF THEM MATTER
    conflict   in both, resolving to DIFFERENT values. The serious one:
               deploying the repo file would change how live modules render.
    missing    in the repo, absent from the deployed file. Any module using
               one is silently living on its fallback.
    orphan     deployed but not in the repo. Usually a token promoted during
               a module build that never came back — the repo is behind, not
               the deployment.
    cosmetic   same resolved value, written differently (the repo aliases a
               primitive where the deployment repeats the hex). Harmless.

Exit code 0 when there are no conflicts and nothing missing; 1 otherwise.
Orphans alone do not fail — they are a backlog, not a breakage.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALIAS = re.compile(r"^var\(\s*(--equinet-[a-z0-9\-]+)\s*(?:,.*)?\)$")


def parse(path):
    """Declarations inside the :root block, in file order."""
    text = open(path, encoding="utf-8", errors="replace").read()
    start = text.find(":root")
    if start == -1:
        return {}
    body = text[start:]
    return {
        m.group(1): re.sub(r"\s+", " ", m.group(2)).strip()
        for m in re.finditer(r"(--equinet-[a-z0-9\-]+)\s*:\s*([^;]+);", body)
    }


def resolve(table, name, depth=0):
    """Follow var() aliases to a literal, so an alias and the hex it points
    at are not reported as a difference."""
    value = table.get(name)
    if value is None or depth > 10:
        return value
    m = ALIAS.match(value)
    return resolve(table, m.group(1), depth + 1) if m else value


def main():
    if len(sys.argv) != 2:
        print("usage: python tools/check-deployed-tokens.py path/to/deployed/tokens.css")
        return 2
    deployed_path = sys.argv[1]
    if not os.path.exists(deployed_path):
        print(f"no such file: {deployed_path}")
        return 2

    repo = parse(os.path.join(ROOT, "tokens.css"))
    dep = parse(deployed_path)

    conflicts, cosmetic = [], []
    for name in sorted(set(repo) & set(dep)):
        r, d = resolve(repo, name), resolve(dep, name)
        if r != d:
            conflicts.append((name, repo[name], r, dep[name]))
        elif repo[name] != dep[name]:
            cosmetic.append(name)

    missing = sorted(set(repo) - set(dep))
    orphans = sorted(set(dep) - set(repo))

    print(f"repo     {os.path.join('tokens.css')}: {len(repo)} tokens")
    print(f"deployed {deployed_path}: {len(dep)} tokens\n")

    if conflicts:
        print(f"CONFLICT — same name, different value ({len(conflicts)})")
        print("  Deploying the repo file would change how live modules render.")
        print("  Decide which value is right before uploading anything.\n")
        for name, raw, r, d in conflicts:
            shown = f"{raw}  →  {r}" if raw != r else raw
            print(f"  {name}")
            print(f"      repo      {shown}")
            print(f"      deployed  {d}")
        print()

    if missing:
        print(f"MISSING — in the repo, not deployed ({len(missing)})")
        print("  A module using one of these is running on its fallback and")
        print("  will not follow a change to the token.\n")
        for name in missing:
            print(f"  {name} = {resolve(repo, name)}")
        print()

    if orphans:
        print(f"ORPHAN — deployed, not in the repo ({len(orphans)})")
        print("  Usually promoted during a module build and never brought back.")
        print("  The repo is behind here, not the deployment.\n")
        for name in orphans:
            print(f"  {name} = {dep[name]}")
        print()

    if cosmetic:
        print(f"COSMETIC — same value, written differently ({len(cosmetic)}): "
              + ", ".join(n.replace("--equinet-", "") for n in cosmetic))
        print("  The repo aliases a primitive where the deployment repeats the")
        print("  literal. No rendering difference; fixed by redeploying.\n")

    bad = len(conflicts) + len(missing)
    print(f"{len(conflicts)} conflict(s), {len(missing)} missing, "
          f"{len(orphans)} orphan(s), {len(cosmetic)} cosmetic.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
