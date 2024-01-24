import React from "react";
import { useNavigate } from "react-router-dom";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Welcome from "./components/Welcome";
import Profile from "./components/Profile";

function HomeComponent() {
  let navigate = useNavigate();

  function navigateToWelcome() {
    navigate("/welcome");
  }

  function navigateToProfile() {
    navigate("/profile");
  }

  return (
    <div>
      <button onClick={navigateToWelcome}>Go to Welcome Page</button>
      <button onClick={navigateToProfile}>Go to Profile Page</button>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomeComponent />} />
        <Route path="/welcome" element={<Welcome />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>
    </Router>
  );
}

export default App;
