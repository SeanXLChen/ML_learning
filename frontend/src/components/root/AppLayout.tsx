import { Outlet } from "react-router-dom";

import Header from "../navigation/Header";

export default AppLayout;

function AppLayout() {
  return (
    <div className="main">
      <Header />
      <div className="content d-flex flex-grow-1">
        <Outlet />
      </div>
    </div>
  );
}
