import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import { svmCaseItems } from "../../../../static/svmCaseItems";
import InteractiveHelper from "../../../helper/interactiveHelper";
import helperContentText from "../../../../static/helperContentText.json";
import "../../../../styles/svm.scss";
import { Select } from 'antd';

export default function SvmCaseStudy() {
  const location = useLocation();
  const [currentPage, setCurrentPage] = useState(
    location.pathname.split("/").pop() || ""
  );
  const [currentSelectedItem, setCurrentSelectedItem] = useState("breast-cancer");

  useEffect(() => {
    setCurrentPage(location.pathname.split("/").pop() || "");
  }, [location]);

  const currentCaseItem = svmCaseItems.find(
    (item) => currentSelectedItem === item.title.toLowerCase().replace(" ", "-")
  );

  const handleChange = (value: string) => {
    setCurrentSelectedItem(value);
  };

  return (
    <div>
        <div className="case-study">
          {/* <p className="case-header">Use Cases</p> */}
          <p className="case-title">Dataset</p>
    <Select
      className="case-selector"
      defaultValue="Breast Cancer"
      style={{ width: 180 }}
      onChange={handleChange}
      options={[
        { value: 'breast-cancer', label: 'Breast Cancer' },
        { value: 'ionosphere', label: 'Ionosphere' },
        { value: 'penguins', label: 'Penguins' },
      ]}
    />
          <p className="case-title">Case Story</p>
          <div className="case-story">{currentCaseItem?.case_story}</div>
          {/* <p className="case-title">Data Details</p> */}
        </div>
        <InteractiveHelper section={helperContentText.svm}/>
    </div>
  );
}
