import React from "react";

function UserStats({ age }) {
  return (
    <div className="card p-3 mb-3">
      <h4>User Statistics</h4>
      <p>
        Status: {age >= 18 ? "Adult" : "Minor"}
      </p>
    </div>
  );
}

export default UserStats;