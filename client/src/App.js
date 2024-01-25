import React from "react";
import { useNavigate } from "react-router-dom";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Welcome from "./components/Welcome";
import Profile from "./components/Profile";
import Utilities from "./components/Utilities";
import Countdown from "./components/CountDown";
import TopBar from "./components/TopBar";
import ExampleComponent from "./components/Example";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import { useTheme } from "@mui/material/styles";

function HomeComponent() {
  const theme = useTheme();

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
    >
      <TopBar />
      <div style={{ height: 100 }}></div>
      <Button
        variant="contained"
        onClick={navigateToWelcome}
        style={{
          backgroundColor: theme.palette.primary.light,
          color: "white",
          marginBottom: 50,
        }}
      >
        Welcome Page
      </Button>
      <Button
        variant="contained"
        color="warning"
        onClick={navigateToProfile}
        style={{
          backgroundColor: theme.palette.secondary.light,
          color: "white",
          marginBottom: 50,
        }}
      >
        Profile Page
      </Button>
      <Button
        variant="contained"
        color="secondary"
        onClick={navigateToExample}
        style={{
          backgroundColor: theme.palette.success.light,
          color: "white",
          marginBottom: 50,
        }}
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
