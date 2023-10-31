import { useState, useEffect } from "react";
import { Menu } from "antd";
import { Link } from "react-router-dom";

import { svmSidebarItems } from "../../../../static/svmSidebarItems";
import "../../../../styles/svm.scss";

export default function SvmNewSidebar() {
  const [svmResults, setSvmResults] = useState<any>(null);
  const [currentPage, setCurrentPage] = useState(
    window.location.pathname.split("/").pop() || ""
  );

  // const generateMenuItems = (items: typeof svmSidebarItems) => {
  //   return items.map((item, index) => {
  //     const subMenuItems = item.submenu.map((subItem, subIndex) => ({
  //       key: `${index}_${subIndex}`,
  //       label: subItem,
  //     }));

  //     return {
  //       key: `${index}`,
  //       label: item.title,
  //       icon: null,
  //       items: subMenuItems,
  //     } as MenuItem;
  //   });
  // };

  const convertSubItemNameToPath = (subItem: string) => {
    return subItem.toLowerCase().replace(" ", "-");
  };

  const handleOnClick = (key: string) => {
    setCurrentPage(convertSubItemNameToPath(key));
    const localData = localStorage.getItem("svm-results");
    setSvmResults(localData);
  };

  useEffect(() => {
    const localData = localStorage.getItem("svm-results");
    setSvmResults(localData);
  }, []);

  return (
    <div>
      <Menu
        className="svm-sidebar-dark"
        defaultSelectedKeys={[currentPage]}
        mode="inline"
        theme="dark"
        onClick={(e) => handleOnClick(e.key)}
      >
        {svmSidebarItems.map((item, index) => (
          <Menu.SubMenu key={index} title={item.title}>
            {item.submenu.map((subItem, subIndex) => (
              <Menu.Item key={`${index}_${subIndex}`}>
                {/* Disable if no results and subItem === "Generated Model" */}
                {subItem === "Generated Model" && !svmResults ? (
                  <span className="disabled-link">Generated Model</span>
                ) : (
                  <Link
                    to={`/learn/supervised/svm/${convertSubItemNameToPath(
                      subItem
                    )}`}
                  >
                    {subItem}
                  </Link>
                )}
              </Menu.Item>
            ))}
          </Menu.SubMenu>
        ))}
      </Menu>
    </div>
  );
};
