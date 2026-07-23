import React from "react";
function UserActions({ onIncrease, onDecrease, onClickCount }) {
    return (
        <div className="text-center mt-3">
            <button className="btn btn-success m-2" onClick={onIncrease}>
                Increase Age
            </button>
            <button className="btn btn-danger m-2" onClick={onDecrease}>
                Decrease Age
            </button>
            <button className="btn btn-warning m-2" onClick={onClickCount}>
                Count Click
            </button>
        </div>
    );
}
export default UserActions;