import { homedir } from "node:os";
import path from "node:path";
import { pathToFileURL } from "node:url";

const EXPECTED_PLAYWRIGHT_VERSION = "1.61.1";
const EXPECTED_CHROMIUM_REVISION = "1228";

export async function launchPinnedChromium(requestedBrowserPath) {
  const runtimeRoot = process.env.ULTIMATE_DESIGN_PLAYWRIGHT_RUNTIME
    || process.env.CODEX_PLAYWRIGHT_RUNTIME
    || path.join(homedir(), ".codex", "playwright-runtime");
  const runtimeModule = pathToFileURL(path.join(runtimeRoot, "runtime.mjs")).href;
  let runtime;
  try {
    runtime = await import(runtimeModule);
  } catch (error) {
    throw new Error(
      `Pinned Playwright runtime unavailable at ${runtimeRoot}. `
      + `Expected Playwright ${EXPECTED_PLAYWRIGHT_VERSION} with Chromium revision ${EXPECTED_CHROMIUM_REVISION}. `
      + "Provision the runtime explicitly and set ULTIMATE_DESIGN_PLAYWRIGHT_RUNTIME; do not fall back to system Chrome.",
      { cause: error },
    );
  }

  if (
    runtime.pinnedRuntime?.playwrightVersion !== EXPECTED_PLAYWRIGHT_VERSION
    || String(runtime.pinnedRuntime?.chromiumRevision) !== EXPECTED_CHROMIUM_REVISION
    || typeof runtime.launchPinnedChromium !== "function"
  ) {
    throw new Error(
      `Pinned Playwright runtime mismatch at ${runtimeRoot}. `
      + `Expected Playwright ${EXPECTED_PLAYWRIGHT_VERSION} with Chromium revision ${EXPECTED_CHROMIUM_REVISION}.`,
    );
  }

  if (
    requestedBrowserPath
    && requestedBrowserPath !== runtime.pinnedRuntime.executablePath
  ) {
    console.warn(
      `Ignoring unpinned browser path: ${requestedBrowserPath}. Using ${runtime.pinnedRuntime.executablePath}`,
    );
  }

  return runtime.launchPinnedChromium();
}
