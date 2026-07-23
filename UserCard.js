import React from "react";

function UserCard({ name, age }) {
  return (
    <div className="card text-center shadow mb-3">
      <div className="card-body">
        <h5>User Details</h5>

        <p>
          <strong>Name:</strong> {name}
        </p>

        <p>
          <strong>Age:</strong> {age}
        </p>
      </div>
    </div>
  );
}

export default UserCard;