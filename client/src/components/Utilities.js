import React, { useState } from "react";
import Navigation from "./Navigation";

function Utilities() {
  const [integer, setInteger] = useState("");
  const [operation, setOperation] = useState("");
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [result, setResult] = useState(null);

  const handleNumberChange = (event) => setInteger(event.target.value);
  const handleOperationChange = (event) => setOperation(event.target.value);

  const handleSubmit = async () => {
    setIsSubmitted(true);
    const response = await fetch("/process-integer", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ integer: parseInt(integer, 10), operation }),
    });

    if (response.ok) {
      const data = await response.json();
      setResult(data.result);
    }
  };

  const handleEdit = () => {
    setIsSubmitted(false);
    setResult(null);
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
      <p>Select an operation:</p>
      <select
        value={operation}
        onChange={handleOperationChange}
        disabled={isSubmitted}
      >
        <option value="">Select an Operation</option>
        <option value="double">Double Integer</option>
        <option value="halve">Halve Integer</option>
        <option value="subtract">Subtract One</option>
        <option value="add">Add Three</option>
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

export default Utilities;
