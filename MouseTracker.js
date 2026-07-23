import React, { Component } from "react";
class MouseTracker extends Component {
  state = { x: 0, y: 0 };
  handleMouseMove = (event) => {
    this.setState({
      x: event.clientX,
      y: event.clientY,
    });
  };
  render() {
    return (
      <div
        style={{ height: "200px", border: "1px solid black" }}
        onMouseMove={this.handleMouseMove}
      >
        {this.props.render(this.state)}
      </div>
    );
  }
}
export default MouseTracker;