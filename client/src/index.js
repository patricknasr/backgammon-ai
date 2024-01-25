import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App"; // or Root, if you named your main component Root

const root = createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
