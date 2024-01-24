import React, { useState } from "react";
import Navigation from "./Navigation";

function Profile() {
  const [color, setColor] = useState("");
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleColorChange = (event) => {
    if (!isSubmitted) {
      setColor(event.target.value);
    }
  };

  const handleSubmit = () => {
    setIsSubmitted(true);
    console.log("Selected Color:", color); // Logs the selected color to the console
  };

  const handleEdit = () => {
    setIsSubmitted(false);
  };

  return (
    <div>
      <Navigation />
      <h1>Profile Page</h1>
      <p>Select a color:</p>
      <select value={color} onChange={handleColorChange} disabled={isSubmitted}>
        <option value="">Select a Color</option>
        <option value="red">Red</option>
        <option value="green">Green</option>
        <option value="yellow">Yellow</option>
        <option value="blue">Blue</option>
      </select>
      <button onClick={handleSubmit} disabled={isSubmitted}>
        Submit
      </button>
      <button onClick={handleEdit} disabled={!isSubmitted}>
        Edit
      </button>
    </div>
  );
}

export default Profile;
