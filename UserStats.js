import React from "react";
function UserStats({ clicks }) {
    return (
        <div className="card text-center shadow mb-3">
            <div className="card-body">
                <h5 className="card-title">User Stats</h5>
                <p className="card-text">
                    <strong>Button Clicks:</strong> {clicks}
                </p>
            </div>
        </div>
    );
}
export default UserStats;