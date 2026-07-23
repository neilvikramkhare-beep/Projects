import React from "react";
function UserCard({ name, age }) {
    return (
        <div className="card text-center shadow mb-3">
            <div className="card-body">
                <h5 className="card-title">User Details</h5>
                <p className="card-text">
                    <strong>Name:</strong> {name}
                </p>
                <p className="card-text">
                    <strong>Age:</strong> {age}
                </p>
            </div>
        </div>
    );
}
export default UserCard;