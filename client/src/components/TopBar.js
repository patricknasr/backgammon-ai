import React from "react";
import { useNavigate } from "react-router-dom";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Button from "@mui/material/Button";

function TopBar() {
  const navigate = useNavigate();

  return (
    <AppBar position="static">
      <Toolbar>
        <Button color="inherit" onClick={() => navigate("/utilities")}>
          Utilities
        </Button>
        <Button color="inherit" onClick={() => navigate("/countdown")}>
          Countdown
        </Button>
      </Toolbar>
    </AppBar>
  );
}

export default TopBar;
