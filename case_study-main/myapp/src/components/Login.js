import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Header from "./Header";

const Login = () => {
  const [email, setemail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const nav = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/login/",
        { email, password },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      const { id, is_manager, manager_id } = response.data;
      console.log(response.data);
      if (is_manager) {
        nav("/manager", { state: { manager_id } });
      } else {
        nav("/employee", { state: { id } });
        console.log("this is from login component" + id);
      }
    } catch (error) {
      setError(error.response.data.error);
      console.log(error.response.data.errror);
    }
  };

  return (
    <div>
      <Header />
      <div className="mt-[200px] flex items-center justify-center">
        <form
          className="p-5 border border-gray-800 flex flex-col rounded-2xl shadow-2xl w-[500px]"
          onSubmit={handleSubmit}
        >
          <h1 className="text-2xl mb-5">Login</h1>
          <input
            type="text"
            placeholder="Email"
            className="p-2 m-2 border border-gray-400 rounded"
            onChange={(e) => setemail(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            className="p-2 m-2 border border-gray-400 rounded"
            onChange={(e) => setPassword(e.target.value)}
          />
          <p className="text-red-500">{error}</p>
          <button
            type="submit"
            className="p-2 m-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
