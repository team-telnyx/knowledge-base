// BASE_PATH is injected at build time (vite.config.ts `define`). Normalize it
// in one place: wouter's router base must not end with a slash (and is "" at
// the root), while fetch/asset URL prefixes always need the trailing slash.
// Keeping both derivations here prevents the three-copies drift where a
// trailing-slash BASE_PATH silently broke routing.
const raw = process.env.BASE_PATH || "/";
const trimmed = raw.endsWith("/") ? raw.slice(0, -1) : raw;

export const routerBase = trimmed;
export const assetBase = `${trimmed}/`;
