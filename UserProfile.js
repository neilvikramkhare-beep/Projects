import React from "react";

function UserProfile({ name, age }) {
  return (
    <div className="card p-3 mb-3">
      <h4>User Profile</h4>
      <p>Name: {name}</p>
      <p>Age: {age}</p>
    </div>
  );
}

export default UserProfile;