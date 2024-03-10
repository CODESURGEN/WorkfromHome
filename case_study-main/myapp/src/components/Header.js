import logo from "./logo.png";
import React from "react";

const Header = () => {
  return (
    <div className="shadow-md">
      <img className="m-2 px-2" src={logo} alt="logo" />
    </div>
  );
};

export default Header;
