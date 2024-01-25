import React from "react";
import { useNavigate } from "react-router-dom";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Welcome from "./components/Welcome";
import Profile from "./components/Profile";
import Utilities from "./components/Utilities";
import Countdown from "./components/CountDown";
import ExampleComponent from "./components/Example";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";

function HomeComponent() {
  let navigate = useNavigate();

  function navigateToWelcome() {
    navigate("/welcome");
  }

  function navigateToProfile() {
    navigate("/profile");
  }

  function navigateToUtilities() {
    navigate("/utilities");
  }

  function navigateToCountDown() {
    navigate("/countdown");
  }

  function navigateToExample() {
    navigate("/example");
  }

  return (
    <Box
      display="flex"
      flexDirection="column"
      alignItems="center"
      justifyContent="center"
      style={{ marginTop: 200 }}
    >
      <Button
        variant="contained"
        color="primary"
        onClick={navigateToWelcome}
        style={{ marginBottom: 50 }}
      >
        Welcome Page
      </Button>
      <Button
        variant="contained"
        color="primary"
        onClick={navigateToProfile}
        style={{ marginBottom: 50 }}
      >
        Profile Page
      </Button>
      <Button
        variant="contained"
        color="primary"
        onClick={navigateToUtilities}
        style={{ marginBottom: 50 }}
      >
        Utilities Page
      </Button>
      <Button
        variant="contained"
        color="primary"
        onClick={navigateToCountDown}
        style={{ marginBottom: 50 }}
      >
        Count Down Page
      </Button>
      <Button
        variant="contained"
        color="primary"
        onClick={navigateToExample}
        style={{ marginBottom: 50 }}
      >
        Example Page
      </Button>
    </Box>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomeComponent />} />
        <Route path="/welcome" element={<Welcome />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/utilities" element={<Utilities />} />
        <Route path="/countdown" element={<Countdown />} />
        <Route path="/example" element={<ExampleComponent />} />
      </Routes>
    </Router>
  );
}

export default App;
