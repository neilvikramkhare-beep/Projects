import React from "react";
function withAuth(Component) {
  return function AuthComponent(props) {
    const isAuthenticated = true;
    if (!isAuthenticated) {
      return <h2>Please login</h2>;
    }
    return <Component {...props} />;
  };
}
export default withAuth;