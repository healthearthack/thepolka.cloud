/**
 * thepolka.cloud Syndication & Portal Interfaces
 * Strict TypeScript contracts for RSS 2.0 items, XML feed generators, and 3D portal telemetry.
 */

export interface RSSItem {
  title: string;
  link: string;
  description: string;
  pubDate: string;
  guid: string;
  creator: string;
  identifier: string;
  categories: string[];
}

export interface RSSChannel {
  title: string;
  link: string;
  description: string;
  language: string;
  lastBuildDate: string;
  atomSelfLink: string;
  managingEditor: string;
  webMaster: string;
  items: RSSItem[];
}

export interface PortalTelemetryState {
  active_doi: string;
  xco2_ppm: number;
  net_enthalpy_mw: number;
  waqf_treasury_usd: number;
  timestamp: string;
}
