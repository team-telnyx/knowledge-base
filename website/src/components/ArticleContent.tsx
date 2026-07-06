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
      >
        {body}
      </ReactMarkdown>
    </div>
  );
});
