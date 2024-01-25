import React, { useState, useEffect } from "react";
import Navigation from "./Navigation";

function CountdownComponent() {
  const [inputValue, setInputValue] = useState("");
  const [count, setCount] = useState(0);
  const [isActive, setIsActive] = useState(false);

  useEffect(() => {
    let interval = null;

    if (isActive && count > 0) {
      interval = setInterval(() => {
        setCount((count) => count - 1);
      }, 1000);
    } else if (count === 0) {
      clearInterval(interval);
    }

    return () => clearInterval(interval);
  }, [isActive, count]);

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSubmit = () => {
    setCount(parseInt(inputValue, 10));
    setIsActive(true);
  };

  return (
    <div>
      <Navigation />
      <input type="number" value={inputValue} onChange={handleInputChange} />
      <button onClick={handleSubmit}>Start Countdown</button>
      <h1>{count}</h1>
    </div>
  );
}

export default CountdownComponent;
