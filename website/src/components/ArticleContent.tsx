import React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";
import "./ArticleContent.css";

export const ArticleContent = React.memo(function ArticleContent({
  body,
}: {
  body: string;
}) {
  return (
    <div className="article-content">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeRaw]}
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
            return <a href={href} {...props}>{children}</a>;
          },
        }}
      >
        {body}
      </ReactMarkdown>
    </div>
  );
});
