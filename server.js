import http from 'http';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

if (process.argv.includes('--check')) {
  const requiredFiles = [
    'tokens.css',
    'tokens.json',
    'components/bundle.css',
    'README.md',
    'index.html'
  ];
  for (const file of requiredFiles) {
    if (!fs.existsSync(path.join(__dirname, file))) {
      console.error(`Missing required file: ${file}`);
      process.exit(1);
    }
  }
  console.log('Equinet Design System build check passed.');
  process.exit(0);
}

const PORT = Number(process.env.PORT) || 3000;

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.md': 'text/plain; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.ico': 'image/x-icon'
};

const ALLOWED_DOCS = {
  'readme': 'README.md',
  'handoff': 'HANDOFF.md',
  'prompt-template': 'PROMPT-TEMPLATE.md',
  'changelog': 'CHANGELOG.md',
  'icon-reference': 'assets/icons/ICON-REFERENCE.md',
  'illustrations-index': 'assets/illustrations/INDEX.md',
  'layout-skill': 'skills/equinet-layout/SKILL.md',
  'visual-kit': 'skills/equinet-layout/references/visual-kit.md'
};

const server = http.createServer((req, res) => {
  try {
    const parsedUrl = new URL(req.url || '/', `http://${req.headers.host || 'localhost'}`);
    let pathname = decodeURIComponent(parsedUrl.pathname);

    // Human-friendly route for the GEO landing page preview.
    if (pathname === '/geo' || pathname === '/geo/') {
      pathname = '/geo.html';
    }

    if (pathname.startsWith('/api/docs/')) {
      const docName = pathname.replace('/api/docs/', '');
      const target = ALLOWED_DOCS[docName];
      if (!target) {
        res.writeHead(404, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Document not found' }));
        return;
      }
      const fullPath = path.join(__dirname, target);
      if (!fs.existsSync(fullPath)) {
        res.writeHead(404, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'File not found' }));
        return;
      }
      res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
      res.end(fs.readFileSync(fullPath, 'utf-8'));
      return;
    }

    let safePath = path.normalize(pathname).replace(/^(\.\.(\/|\\|$))+/, '');
    if (safePath === '/' || safePath === '') {
      safePath = '/index.html';
    }

    const filePath = path.join(__dirname, safePath);
    if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
      const ext = path.extname(filePath).toLowerCase();
      const contentType = MIME_TYPES[ext] || 'application/octet-stream';
      res.writeHead(200, { 'Content-Type': contentType });
      fs.createReadStream(filePath).pipe(res);
      return;
    }

    // SPA fallback to index.html
    const indexPath = path.join(__dirname, 'index.html');
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    fs.createReadStream(indexPath).pipe(res);
  } catch (err) {
    res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('Internal Server Error');
  }
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`Equinet Design System running at http://0.0.0.0:${PORT}`);
});
