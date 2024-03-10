import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Login";
import Manager from "./Manager";
import Employee from "./Employee";
import WFH from "./WFH";

const Body = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/manager" element={<Manager />} />
          <Route path="/employee" element={<Employee />} />
          <Route path="/WFH" element={<WFH />} />
        </Routes>
      </div>
    </Router>
  );
};

export default Body;
