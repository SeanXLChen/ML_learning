import {
  AiOutlineClose,
  AiOutlineReload,
} from "react-icons/ai";
import "../../styles/helper.scss";
import { useState } from "react";

interface SubSection {
  section: string;
  response: string[];
  furtherResources: string[];
}

interface ContentItem {
  section: string;
  response: string[];
  furtherResources: string[];
  subSection: SubSection[];
}

interface HelperContentProps {
  isVisible: boolean;
  onClick: () => void;
  content: ContentItem[];
}

export default function HelperContent({
  onClick,
  isVisible,
  content,
}: HelperContentProps) {
  const [selectedSection, setSelectedSection] = useState<ContentItem | null>(
    null
  );
  const [selectedSubSection, setSelectedSubSection] =
    useState<SubSection | null>(null);

  const handleSectionOnClick = (section: ContentItem) => {
    setSelectedSection(section);
  };

  const hangleSubSectionOnClick = (subSection: SubSection) => {
    setSelectedSubSection(subSection);
  };

  const handleGoBack = () => {
    if (selectedSection && selectedSubSection) {
      setSelectedSubSection(null);
    } else {
      setSelectedSection(null);
      setSelectedSubSection(null);
    }
  };

  const displaySections = () => (
    <div className="helper-button-container">
      {content.map((item) => (
        <button
          key={item.section}
          className="helper-button"
          onClick={() => handleSectionOnClick(item)}
        >
          {item.section}
        </button>
      ))}
    </div>
  );

  const displaySubSections = () => (
    <div className="helper-button-container">
      {selectedSection?.subSection.map((item) => (
        <button
          key={item.section}
          className="helper-button"
          onClick={() => hangleSubSectionOnClick(item)}
        >
          {item.section}
        </button>
      ))}
    </div>
  );

  const displayResponse = (selected: ContentItem | SubSection) => (
    <div>
      {selected && (
        <div>
          <div className="right-side">{selected.section}</div>
          <div className="left-side">
            {selected.response.map((item) => (
              <p>{item}</p>
            ))}
            <p>For additional reading, you can explore these websites:</p>
            {selected.furtherResources.map((item) => (
              <ul>
                <li>
                  <a href={item} target="_blank" rel="noopener noreferrer">{item}</a>
                </li>
              </ul>
            ))}
          </div>
        </div>
      )}
    </div>
  );

  const displayGoBackButton = () => (
    <div className="go-back">
      <button
        className="helper-button"
        onClick={() => {
          handleGoBack();
        }}
      >
        Go Back
      </button>
    </div>
  );

  const displayContent =
    content.length > 0 ? (
      <div>
        <div className="left-side">
          {/* <AiOutlineRobot style={{fontSize: '25px'}} /> */}
          <p>Hi, how can I help you?</p>
        </div>
        {!selectedSection && displaySections()}
        {selectedSection && displayResponse(selectedSection)}
        {selectedSection &&
          selectedSection?.subSection.length > 0 &&
          !selectedSubSection &&
          displaySubSections()}
        {selectedSubSection && displayResponse(selectedSubSection)}
        {(selectedSection || selectedSubSection) && displayGoBackButton()}
      </div>
    ) : (
      <div>The content is under construction.</div>
    );

  const handleRefresh = () => {
    setSelectedSection(null);
    setSelectedSubSection(null);
  };

  return (
    <div className={`helper-content-container ${isVisible ? "visible" : ""}`}>
      <div className="helper-header">
        <p className="helper-title">Dashboard Helper</p>
        <div className="button-container">
          <button className="refresh-button" onClick={handleRefresh}>
            <AiOutlineReload />
          </button>
          <button className="close-button" onClick={onClick}>
            <AiOutlineClose />
          </button>
        </div>
      </div>
      <div className="helper-content">{displayContent}</div>
    </div>
  );
}
