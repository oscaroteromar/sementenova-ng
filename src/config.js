// Nullish coalescing (not ||): an explicitly-set empty string means
// "same origin" (e.g. behind the docker-compose Caddy proxy) and must
// not fall back to the default.
export const API_BASE = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'
