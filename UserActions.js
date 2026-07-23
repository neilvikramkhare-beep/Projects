import React from "react";

function UserActions({ updateAge }) {
  return (
    <div className="text-center mb-3">
      <button className="btn btn-success" onClick={updateAge}>
        Increase Age
      </button>
    </div>
  );
}

export default UserActions;