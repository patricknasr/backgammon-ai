import React, { useState } from "react";
import Navigation from "./Navigation";

function Profile() {
  const [integer, setInteger] = useState("");
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [result, setResult] = useState(null); // Added state to store the result

  const handleNumberChange = (event) => {
    if (!isSubmitted) {
      setInteger(event.target.value);
    }
  };

  const handleSubmit = async () => {
    setIsSubmitted(true);
    console.log("Selected Number:", integer); // Logs the selected color to the console

    // Make a POST request to your Flask backend
    const response = await fetch("/process-integer", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ integer }),
    });

    if (response.ok) {
      const data = await response.json();
      setResult(data.result);
    }
  };

  const handleEdit = () => {
    setIsSubmitted(false);
    setResult(null); // Reset the result when editing
  };

  return (
    <div>
      <Navigation />
      <h1>Utilities Page</h1>
      <p>Select a number:</p>
      <select
        value={integer}
        onChange={handleNumberChange}
        disabled={isSubmitted}
      >
        <option value="">Select a Number</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>
        <option value="8">8</option>
        <option value="9">9</option>
      </select>
      <button onClick={handleSubmit} disabled={isSubmitted}>
        Submit
      </button>
      <button onClick={handleEdit} disabled={!isSubmitted}>
        Edit
      </button>
      {result !== null && <p>Result: {result}</p>}
    </div>
  );
}

export default Profile;
