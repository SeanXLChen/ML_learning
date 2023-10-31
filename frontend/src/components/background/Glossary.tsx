import ContentRenderer from "../root/ContentRenderer";
import staticContent from "../../static/staticContent.json";
import "../../styles/background.scss";

export default function Glossary() {
  return <div className="glossary">
    <ContentRenderer content={staticContent.glossary} />
  </div>;
}
