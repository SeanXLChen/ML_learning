import "../../styles/background.scss";
import { Link } from "react-router-dom";
import ContentRenderer from "../root/ContentRenderer";
import staticContent from "../../static/staticContent.json";

export default function Principles() {
  return <div className="principles">
    <ContentRenderer content={staticContent.principlesTopSection} />
    <div className="content-container">
      <div className="content-card">
        <Link to="/eda">
          <button className="ml-pipeline">Data Exploration and Preprocessing</button>
        </Link>
      </div>
      <div className="content-card">
        <Link to="/learn">
          <button className="ml-pipeline">Model Build</button>
        </Link>
      </div>
      <div className="content-card">
        <Link to="/learn">
        <button className="ml-pipeline">Model Evaluation and Tuning</button>
        </Link>
      </div>
    </div>
    <ContentRenderer content={staticContent.principlesSecondSection} />
  </div>;
}
