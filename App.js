import React, { useState } from "react";

import Header from "./Header";
import UserCard from "./UserCard";
import UserProfile from "./UserProfile";
import UserStats from "./UserStats";
import UserActions from "./UserActions";
import UserList from "./UserList";

function App() {
  const [user, setUser] = useState({
    name: "John Doe",
    age: 25
  });

  const updateAge = () => {
    setUser({
      ...user,
      age: user.age + 1
    });
  };

  return (
    <div className="container mt-4">
      <Header />

      <UserCard
        name={user.name}
        age={user.age}
      />

      <UserProfile
        name={user.name}
        age={user.age}
      />

      <UserStats age={user.age} />

      <UserActions updateAge={updateAge} />

      <UserList />
    </div>
  );
}

export default App;