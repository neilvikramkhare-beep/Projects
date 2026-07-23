import React, { useState } from "react";
function MouseTracker({ render }) {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const handleMouseMove = (event) => {
    setPosition({
      x: event.clientX,
      y: event.clientY
    });
  };
}
export default MouseTracker;