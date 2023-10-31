import { menuItems } from "../../static/menuItems";
import MenuItems from "./MenuItems";

export default function Navbar() {
  return (
    <nav>
      <ul className="menus">
        {menuItems.map((item) => {
          const depthLevel = 0;
          return (
            <MenuItems key={item.title} items={item} depthLevel={depthLevel} />
          );
        })}
      </ul>
    </nav>
  );
}
