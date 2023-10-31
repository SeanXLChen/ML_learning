import { useState, useEffect, useRef } from "react";
import { Link } from "react-router-dom";

import Dropdown from "./Dropdown";

interface SubmenuItem {
  title: string;
  path: string;
}

interface MenuItem {
  title: string;
  path: string;
  submenu?: SubmenuItem[];
}

interface MenuItemsProps {
  items: MenuItem;
  depthLevel: number;
}

export default function MenuItems({ items, depthLevel }: MenuItemsProps) {
  const [dropdown, setDropdown] = useState(false);
  let ref = useRef<HTMLLIElement>(null);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent | TouchEvent) => {
      if (
        dropdown &&
        ref.current &&
        !ref.current.contains(event.target as Node)
      ) {
        setDropdown(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    document.addEventListener("touchstart", handleClickOutside);
    return () => {
      // Cleaup the event listener
      document.removeEventListener("mousedown", handleClickOutside);
      document.removeEventListener("touchstart", handleClickOutside);
    };
  }, [dropdown]);

  return (
    <li
      className="menu-items"
      ref={ref}
      onMouseEnter={() => window.innerWidth > 960 && setDropdown(true)}
      onMouseLeave={() => window.innerWidth > 960 && setDropdown(false)}
    >
      {items.submenu ? (
        <>
          <button
            type="button"
            aria-haspopup="menu"
            aria-expanded={dropdown ? "true" : "false"}
            onClick={() => setDropdown((prev) => !prev)}
          >
            <div>
              {items.title}{" "}
              {depthLevel > 0 ? (
                <span>&raquo;</span>
              ) : (
                <span className="arrow" />
              )}
            </div>
          </button>
          <Dropdown
            submenus={items.submenu}
            dropdown={dropdown}
            depthLevel={depthLevel}
          />
        </>
      ) : (
        <Link to={items.path}>{items.title}</Link>
      )}
    </li>
  );
}
