import React, { useContext } from "react";
import { AppContext } from "../context/AppContext";
const UserProfile = () => {
  const { user, theme, toggleTheme } = useContext(AppContext);
  return (
    <div className={`card mt-3 ${theme === "dark" ? "bg-dark text-white" : ""}`}>
      <div className="card-body">
        <h4>User Profile</h4>
        <p>Username: {user}</p>
        <button className="btn btn-primary" onClick={toggleTheme}>
          Toggle Theme
        </button>
      </div>
    </div>
  );
};
export default UserProfile;