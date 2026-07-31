import { fileURLToPath } from "node:url";
import { defineConfig } from "vitest/config";

export default defineConfig({
  root: fileURLToPath(new URL(".", import.meta.url)),
  test: {
    include: ["**/*.test.ts"],
    exclude: ["./**/*.live.test.ts", "./node_modules/**", "./dist/**"],
    testTimeout: 30_000,
  },
});
