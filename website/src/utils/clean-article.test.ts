import { expect, test } from "bun:test";
import { stripFeedbackTrailer } from "./clean-article";

test("removes the scraped footer when a related link has a bracketed title", () => {
  const body = `Useful article content.

---

Related Articles

[First article](https://support.telnyx.com/en/articles/1-first)[[BETA] Another guide](https://support.telnyx.com/en/articles/2-beta-guide)

Did this answer your question?

😞😐😃`;

  expect(stripFeedbackTrailer(body)).toBe("Useful article content.");
});

test("keeps an authored Related Articles section", () => {
  const body = `Useful article content.\n\n## Related Articles\n\n- [A guide](https://support.telnyx.com/en/articles/1-a-guide)`;
  expect(stripFeedbackTrailer(body)).toBe(body);
});
