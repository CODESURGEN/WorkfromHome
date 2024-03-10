import React, { useEffect, useState } from "react";
import axios from "axios";
import Header from "./Header";
import { useLocation, useNavigate } from "react-router-dom";

const Employee = () => {
  const location = useLocation();
  const id = location.state?.id;
  const [emp, setEmp] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchEmp = async () => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/employees/${id}`
        );
        if (response.data) {
          setEmp(response.data);
        } else {
          console.error("No data received from the API");
        }
      } catch (error) {
        console.error("Error fetching employee:", error);
      }
    };
    fetchEmp();
  }, [id]);

  const WFH = () => {
    navigate("/WFH");
  };

  return (
    <div>
      <Header />
      <div className="container mx-auto p-4">
        <div className="flex justify-between items-center">
          <h1 className="text-3xl font-bold mb-6">Employee Details</h1>
          <button
            onClick={WFH}
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full focus:outline-none focus:shadow-outline-blue"
          >
            Work From Home Request
          </button>
        </div>
        {emp && (
          <div>
            {/* Employee Details Card */}
            <div className="bg-white rounded-lg shadow-md p-6 mb-8">
              <h2 className="text-xl font-bold mb-4">Employee Information</h2>

              <div className="bg-gray-200 rounded-lg p-4">
                <p className="text-gray-700">
                  <span className="font-semibold text-blue-600">Name:</span>{" "}
                  {emp.employee.name}
                </p>
                <p className="text-gray-700">
                  <span className="font-semibold">Email:</span>{" "}
                  {emp.employee.email}
                </p>
                <p className="text-gray-700">
                  <span className="font-semibold">Phone:</span>{" "}
                  {emp.employee.phone}
                </p>
                <p className="text-gray-700">
                  <span className="font-semibold">Department:</span>{" "}
                  {emp.employee.department}
                </p>
                <p className="text-gray-700">
                  <span className="font-semibold">Is Manager:</span>{" "}
                  {emp.employee.is_manager ? "Yes" : "No"}
                </p>
              </div>
            </div>

            {/* Project Details Card */}
            <div className="bg-white rounded-lg shadow-md p-6 mb-8">
              <h2 className="text-xl font-bold mb-4">Project Details</h2>
              <ul>
                {emp.projects.map((project) => (
                  <li key={project.id} className="mb-4">
                    <div className="bg-gray-200 rounded-lg p-4">
                      <p className="font-semibold text-blue-600">
                        Project Name - {project.name}
                      </p>
                      <p className="text-gray-700">
                        Project Desc - {project.description}
                      </p>
                      <p className="text-gray-700">
                        Project Status - {project.status}
                      </p>
                      <p className="text-gray-700">
                        Assigned Employees -{" "}
                        {project.assigned_employees.join(", ")}
                      </p>
                    </div>
                  </li>
                ))}
              </ul>
            </div>

            {/* Manager Details Card */}
            <div className="bg-white rounded-lg shadow-md p-6 mb-8">
              <h2 className="text-xl font-bold mb-4">Manager Details</h2>
              <ul>
                {emp.project_manager.map((manager) => (
                  <li key={manager.id} className="mb-4">
                    <div className="bg-gray-200 rounded-lg p-4">
                      <p className="font-semibold text-blue-600">
                        Manager Name - {manager.name}
                      </p>
                      <p className="text-gray-700">Email - {manager.email}</p>
                      <p className="text-gray-700">
                        Projects - {manager.projects.join(", ")}
                      </p>
                    </div>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Employee;
