import React from "react";
import MouseTracker from "../renderProps/MouseTracker";
const Dashboard = () => {
  return (
    <div className="container mt-4">
      <h2>Dashboard</h2>
      <MouseTracker
        render={({ x, y }) => (
          <h5>
            Mouse Position: {x}, {y}
          </h5>
        )}
      />
    </div>
  );
};
export default Dashboard;