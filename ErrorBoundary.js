import React, { Component } from "react";
class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }
  static getDerivedStateFromError() {
    return { hasError: true };
  }
  componentDidCatch(error, info) {
    console.log("Error caught:", error, info);
  }
  render() {
    if (this.state.hasError) {
      return (
        <div className="alert alert-danger">
          Something went wrong in this component.
        </div>
      );
    }
    return this.props.children;
  }
}
export default ErrorBoundary;