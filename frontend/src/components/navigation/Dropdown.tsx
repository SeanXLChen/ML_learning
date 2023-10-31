import MenuItems from "./MenuItems";

interface DropdownProps {
  submenus: SubmenuItem[];
  dropdown: boolean;
  depthLevel: number;
}

interface SubmenuItem {
  title: string;
  path: string;
  submenu?: SubmenuItem[];
}

export default function Dropdown({ submenus, dropdown, depthLevel }: DropdownProps) {
  depthLevel = depthLevel + 1;
  const dropdownClass = depthLevel > 1 ? "dropdown-submenu" : "";
  return (
    <ul className={`dropdown ${dropdownClass} ${dropdown ? "show" : ""}`}>
      {submenus.map((item: SubmenuItem) => (
        <MenuItems key={item.title} items={item} depthLevel={depthLevel} />
      ))}
    </ul>
  );
}
