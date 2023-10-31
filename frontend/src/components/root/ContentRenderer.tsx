//This is to render content for static pages, including background, glossary, introduction to svm and the svm use cases

import React from "react";

interface ContentRendererProps {
  content: {
    title: string;
    subtitle: Array<{
      title: string;
      content:
        | string
        | string[]
        | Array<{ "section-title": string; "section-content": string | string[] }>;
    }>;
    source?: string | string[];
  };
}

const ContentRenderer: React.FC<ContentRendererProps> = ({ content }) => {
  return (
    <div className="static-content">
      {content.subtitle.map((section, index) => (
        <div key={index} className="content-section">
          <p className="static-content-subtitle">{section.title}</p>
          {Array.isArray(section.content) ? (
            <ul>
              {section.content.map((item, itemIndex) => (
                <li key={itemIndex}>
                  {typeof item === "string" ? (
                    item
                  ) : (
                    <>
                      {item["section-title"] !== "" && (
                        <div className="section-title"><strong>{item["section-title"]}</strong></div>
                      )}
                      {Array.isArray(item["section-content"]) ? (
                        <ul>
                          {item["section-content"].map((subItem, subItemIndex) => (
                            <li key={subItemIndex}>{subItem}</li>
                          ))}
                        </ul>
                      ) : (
                        item["section-content"]
                      )}
                    </>
                  )}
                </li>
              ))}
            </ul>
          ) : (
            <p>{section.content}</p>
          )}
        </div>
      ))}

      {content.source && (
        <div className="static-content-footer">
          <p>Source</p>
          {Array.isArray(content.source) ? (
            <ul>
              {content.source.map((source, sourceIndex) => (
                <li key={sourceIndex}>{source}</li>
              ))}
            </ul>
          ) : (
            <p>{content.source}</p>
          )}
        </div>
      )}
    </div>
  );
};

export default ContentRenderer;
