import React, { useState } from "react";
const UserCard = ({ name, age }) => (
    <div className="card p-3 mb-3">
        <h3>User: {name}</h3>
        <p>Age: {age}</p>
    </div>
);
const UserStats = ({ clicks }) => (
    <div className="alert alert-info">Total Button Clicks: {clicks}</div>
);

const UserActions = ({ onIncrease, onDecrease, onClickCount }) => (
    <div className="d-flex gap-2">
        <button className="btn btn-primary" onClick={() => { onIncrease(); onClickCount(); }}>Age +1</button>
        <button className="btn btn-danger" onClick={() => { onDecrease(); onClickCount(); }}>Age -1</button>
    </div>
);
export default function App() {
    const [user, setUser] = useState({ name: "Alex", age: 25, clicks: 0 });
    const updateAge = () => setUser({ ...user, age: user.age + 1 });
    const decreaseAge = () => setUser({ ...user, age: user.age - 1 });
    const incrementClicks = () => setUser({ ...user, clicks: user.clicks + 1 });
    return (
        <div className="container mt-5">
            <h2 className="text-center mb-4">React Props & State Example</h2>
            <UserCard name={user.name} age={user.age} />
            <UserStats clicks={user.clicks} />
            <UserActions
                onIncrease={updateAge}
                onDecrease={decreaseAge}
                onClickCount={incrementClicks}
            />
        </div>
    );
}