import { expect, test } from "bun:test";
import { articles } from "../../src/content/manifest";

test("unlisted imported articles retain indexing policy through content generation", () => {
  for (const id of ["2819215","9670281","9118675","2807944","8380587","8173789","8008542","1130726","1130719"]) {
    const article = articles.find(a => a.slug.startsWith(id + "-"));
    expect(article).toBeDefined();
    expect(article?.robots).toBe("noindex,nofollow");
  }
  for (const id of ["8159875","10523949"]) {
    const article = articles.find(a => a.slug.startsWith(id + "-"));
    expect(article).toBeDefined();
    expect(article?.robots).toBeUndefined();
  }
});
