import React from "react";

function UserList() {
  const users = [
    { id: 1, name: "John", age: 25 },
    { id: 2, name: "Alice", age: 22 },
    { id: 3, name: "Bob", age: 28 }
  ];

  return (
    <div className="card p-3">
      <h4>User List</h4>

      {users.map((user) => (
        <div key={user.id}>
          {user.name} - {user.age} years
        </div>
      ))}
    </div>
  );
}

export default UserList;