/**
 * thepolka.cloud Express Server
 * Serves the public web portal, 3D digital advertising engine, and W3C RSS 2.0 feed.
 */

import express, { Request, Response } from 'express';
import path from 'path';
import fs from 'fs';

const app = express();
const PORT = process.env.PORT || 8080;

// Resolve static assets: prioritize local public/, fallback to workspace portal/
const localPublic = path.join(__dirname, '..', 'public');
const workspacePortal = path.join(__dirname, '..', '..', 'portal');
const staticRoot = fs.existsSync(path.join(localPublic, 'index.html')) ? localPublic : workspacePortal;

app.use(express.static(staticRoot));

// Route for W3C RSS 2.0 Feed
app.get('/feed.xml', (req: Request, res: Response) => {
  const feedPath = path.join(__dirname, '..', 'feed.xml');
  if (fs.existsSync(feedPath)) {
    res.set('Content-Type', 'application/rss+xml; charset=UTF-8');
    return res.sendFile(feedPath);
  }
  res.status(404).send('Feed not found');
});

// Route for Portal JSON Telemetry API
app.get('/api/portal/status', (req: Request, res: Response) => {
  res.json({
    portal: 'thepolka.cloud',
    subdomain: 'go.thepolka.cloud',
    status: 'OPERATIONAL',
    active_monograph_doi: '10.5281/zenodo.1089a34cc930',
    google_city_cloud_engine: 'ONLINE',
    sovereign_namespaces: ['.oil', '.h2o'],
    static_root: staticRoot,
    timestamp: new Date().toISOString()
  });
});

// Endpoint: .oil Subsurface Telemetry Grid
app.get(['/telemetry/oil', '/api/telemetry/oil'], (req: Request, res: Response) => {
  const manifestPath = path.join(__dirname, '..', '..', 'smackover-oil-lithium-energy', 'domains', 'oil_infrastructure_manifest.json');
  if (fs.existsSync(manifestPath)) {
    return res.json(JSON.parse(fs.readFileSync(manifestPath, 'utf-8')));
  }
  res.json({
    tld: ".oil",
    domain: "smackover.oil",
    status: "ACTIVE_STREAMING",
    reservoir_depth_m: 3200.0,
    net_power_mw_e: 1.95,
    timestamp: new Date().toISOString()
  });
});

// Endpoint: .h2o Water Sovereignty & Desalination Grid
app.get(['/telemetry/h2o', '/api/telemetry/h2o'], (req: Request, res: Response) => {
  const manifestPath = path.join(__dirname, '..', '..', 'crescent-vets-energy-initiative', 'domains', 'h2o_sovereignty_manifest.json');
  if (fs.existsSync(manifestPath)) {
    return res.json(JSON.parse(fs.readFileSync(manifestPath, 'utf-8')));
  }
  res.json({
    tld: ".h2o",
    domain: "freshwater.h2o",
    annual_distilled_gallons: 1277500.0,
    governance: "ALGORITHMIC_WAQF_ENDOWMENT",
    timestamp: new Date().toISOString()
  });
});

if (process.env.NODE_ENV !== 'test') {
  app.listen(PORT, () => {
    console.log(`🌐 thepolka.cloud server running on http://localhost:${PORT}`);
    console.log(`📡 Serving static portal from: ${staticRoot}`);
    console.log(`📡 RSS 2.0 feed available at http://localhost:${PORT}/feed.xml`);
  });
}

export default app;
