import { Button, Card} from "react-bootstrap";
import { useState } from "react";
import { Link } from "react-router-dom";
import "../../../../styles/svm.scss";
import { svmSidebarItems } from "../../../../static/svmSidebarItems";

export default function SvmSidebar() {
  const [showNav, setShowNav] = useState(false);
  const [currentPage, setCurrentPage] = useState(
    window.location.pathname.split("/").pop() || ""
  );

  const convertSubItemNameToPath = (subItem: string) => {
    return subItem.toLowerCase().replace(" ", "-");
  };

  const handleOnClick = (subItem: string) => {
    setCurrentPage(convertSubItemNameToPath(subItem));
  };

  const toggleNavItems = () => {
    setShowNav(!showNav);
  };

  return (
    <div className="svm-sidebar-container">
      <Card className="svm-sidebar-card">
        <div className={`sidebar ${showNav && "active"}`}>
          <Card.Header className="svm-sidebar-title">Support Vector Machine</Card.Header>
          {svmSidebarItems.map((item, index) => (
            <div key={index}>
              <div className="sidebar-title">{item.title}</div>
              {item.submenu.map((subItem, subIndex) => (
                <div className="sidebar-items" key={subIndex}>
                  <Link
                    to={`/learn/supervised/svm/${convertSubItemNameToPath(
                      subItem
                    )}`}
                  >
                    <Button
                      className={`sidebar-button ${
                        currentPage === convertSubItemNameToPath(subItem)
                          ? "active-button"
                          : ""
                      }`}
                      onClick={() => handleOnClick(subItem)}
                    >
                      {subItem}
                    </Button>
                  </Link>
                </div>
              ))}
            </div>
          ))}
        </div>
      </Card>
      {/* <div className="toggle">
        <button className="toggle-button" onClick={toggleNavItems}>
          <RxHamburgerMenu size={30} />
        </button>
      </div> */}
    </div>
  );
}
