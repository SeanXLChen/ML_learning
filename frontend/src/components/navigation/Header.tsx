import { Link } from "react-router-dom";

import "../../styles/app.scss";
import Navbar from "./Navbar";

export default function Header() {
  return (
    <header>
      <div className="nav-area">
        <Link to="/" className="logo">
          Machine Learning Dashboard
        </Link>
        <Navbar />
      </div>
    </header>
  );
}
