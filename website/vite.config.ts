import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

const basePath = process.env.BASE_PATH || "/";

export default defineConfig({
  base: basePath,
  define: {
    "process.env.BASE_PATH": JSON.stringify(basePath),
  },
  server: {
    host: "0.0.0.0",
    port: 5173,
  },
  plugins: [react()],
});
