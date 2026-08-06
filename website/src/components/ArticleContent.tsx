import React from "react";
import { Link } from "wouter";
import ReactMarkdown, { defaultUrlTransform } from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";
import rehypeSanitize from "rehype-sanitize";
import "./ArticleContent.css";

const rawBasePath = process.env.BASE_PATH || "/";
const basePath = rawBasePath.endsWith("/") ? rawBasePath : `${rawBasePath}/`;

// Image references are relative (_images/<hash>.<ext>), which would resolve
// against the current route (/article/<slug>/...) and 404. The files are
// served from the site root, so rewrite them to base-absolute URLs.
function urlTransform(url: string): string | null | undefined {
  if (url.startsWith("_images/")) return `${basePath}${url}`;
  return defaultUrlTransform(url);
}

export const ArticleContent = React.memo(function ArticleContent({
  body,
}: {
  body: string;
}) {
  return (
    <div className="article-content">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeRaw, rehypeSanitize]}
        urlTransform={urlTransform}
        components={{
          a: ({ href, children, ...props }) => {
            const isExternal =
              href && (href.startsWith("http://") || href.startsWith("https://"));
            if (isExternal) {
              return (
                <a href={href} target="_blank" rel="noopener noreferrer" {...props}>
                  {children}
                </a>
              );
            }
            // Rewritten article cross-links navigate client-side.
            if (href?.startsWith("/article/")) {
              return (
                <Link to={href} {...props}>
                  {children}
                </Link>
              );
            }
            return <a href={href} {...props}>{children}</a>;
          },
        }}
      >
        {body}
      </ReactMarkdown>
    </div>
  );
});
