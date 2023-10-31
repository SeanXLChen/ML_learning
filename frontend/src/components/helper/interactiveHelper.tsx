import { useEffect, useState } from "react";
import { AiOutlineQuestion } from "react-icons/ai";
import { useLocation } from "react-router-dom";
import HelperContent from "./helperContent";
import "../../styles/helper.scss";

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

interface PageContent {
  page: string;
  content: ContentItem[];
}

interface InteractiveHelperProps {
  section: {
    content: PageContent[];
  };
}

export default function InteractiveHelper({ section }: InteractiveHelperProps) {
  const [isContentVisible, setIsContentVisible] = useState(false);
  const location = useLocation();
  const currentPage = location.pathname.split("/").pop() || "";
  const [helperContent, setHelperContent] = useState<ContentItem[]>([]);

  const handleButtonOnClick = () => {
    setIsContentVisible(!isContentVisible);
  };

  const handleCloseContent = () => {
    setIsContentVisible(false);
  };

  useEffect(() => {
    setIsContentVisible(false);
    const matchContent = section.content.find((item) => item.page === currentPage); 
    setHelperContent(matchContent ? matchContent.content : []);
  }, [currentPage, section]);

  return (
    <div>
      <button className="helperButton" onClick={() => handleButtonOnClick()}>
        <AiOutlineQuestion />
      </button>
      <HelperContent
        onClick={handleCloseContent}
        isVisible={isContentVisible}
        content={helperContent}
      />
    </div>
  );
}
