import { Outlet } from "react-router-dom";
import { useEffect, useState } from "react";

// import SvmSidebar from "./svm/SvmSidebar";
import "../../../styles/svm.scss";
import SvmNewSidebar from "./svm/SvmSidebarVer2";

export default function SupportVectorMachine() {

  return (
    <div className="support-vector-machine">
      {/* <SvmSidebar /> */}
      <SvmNewSidebar/>
      <Outlet />
    </div>
  );
}
