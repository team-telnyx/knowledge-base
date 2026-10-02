import { expect, test } from "bun:test";
import type { Collection } from "../content/types";
import { collectionArticleCounts } from "./collection-articles";
import { collections, articles } from "../content/manifest";

test("counts descendant articles once and excludes missing articles", () => {
  const fixture = (path: string, childCollectionPaths: string[], articleSlugs: string[]) => ({
    path, childCollectionPaths, articleSlugs,
  } as Collection);
  const counts = collectionArticleCounts([
    fixture("root", ["child", "empty", "missing"], ["a"]),
    fixture("child", ["grandchild"], ["a", "b"]),
    fixture("grandchild", [], ["c", "unavailable"]),
    fixture("empty", [], []),
  ], ["a", "b", "c"].map((slug) => ({ slug })));
  expect(Object.fromEntries(counts)).toEqual({ root: 3, child: 3, grandchild: 1, empty: 0 });
});

test("counts the recovered Voice API and IoT collections", () => {
  const counts = collectionArticleCounts(collections, articles);
  expect(counts.get("133140-voice-api-essentials")).toBe(15);
  expect(counts.get("1895859-telnyx-global-iot-sims")).toBe(21);
  expect(counts.get("133103-telnyx-sms-guide")).toBe(294);
});
