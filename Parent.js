import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Greeting, DisplayCount, TodoList, ToggleContent } from './Child';
function Parent()
 {
  const [count, setCount] = useState(0);
  const [isVisible, setIsVisible] = useState(false);
  const todos = ['Learn React', 'Build a project', 'Deploy the app'];
  return (
    <div className="container mt-5">
      <motion.header 
        className="p-4 mb-4 bg-dark text-white rounded"
        initial={{ scale: 0.9 }}
        animate={{ scale: 1 }}
      >
        <h1>Modular React App</h1>
      </motion.header>
      <Greeting name="Modern Developer" />
      <div className="row mt-4">
        {}
        <div className="col-md-6 mb-3">
          <div className="p-3 bg-light border rounded">
            <p>Current count: <strong>{count}</strong></p>
            <DisplayCount countValue={count} />
            <button 
              onClick={() => setCount(count + 1)} 
              className="btn btn-success"
            >
              Increment
            </button>
          </div>
        </div>
        {}
        <div className="col-md-6 mb-3">
          <div className="p-3 bg-warning border rounded">
            <h4>Animation Toggle</h4>
            <button 
              onClick={() => setIsVisible(!isVisible)} 
              className="btn btn-secondary"
            >
              {isVisible ? 'Hide' : 'Show'}
            </button>
            <ToggleContent isVisible={isVisible} />
          </div>
        </div>
        {}
        <div className="col-12">
          <TodoList items={todos} />
        </div>
      </div>
    </div>
  );
}
export default Parent;