import React from "react";
import { useNavigate } from "react-router-dom";

function Navigation() {
  let navigate = useNavigate();

  return (
    <nav>
      <button onClick={() => navigate("/")}>Home</button>
    </nav>
  );
}

export default Navigation;
