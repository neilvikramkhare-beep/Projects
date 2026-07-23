import React from "react";
const withLoader = (WrappedComponent) => {
  return function WithLoaderComponent({ isLoading, ...props }) {
    if (isLoading) {
      return (
        <div className="text-center mt-4">
          <div className="spinner-border text-primary"></div>
        </div>
      );
    }
    return <WrappedComponent {...props} />;
  };
};
export default withLoader;