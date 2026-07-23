import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
export const Greeting = ({ name }) => (
  <motion.h2 
    className="text-primary"
    initial={{ opacity: 0, y: -10 }}
    animate={{ opacity: 1, y: 0 }}
  >
    Hello, {name}!
  </motion.h2>
);
export const DisplayCount = ({ countValue }) => (
  <p className="text-info">
    The count value passed as a prop is: {countValue}
  </p>
);
export const TodoList = ({ items }) => (
  <div className="p-3 mb-2 bg-danger text-white rounded">
    <h4>Todo List</h4>
    <ul className="list-group">
      {items.map((todo, index) => (
        <motion.li 
          key={index} 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: index * 0.1 }}
          className="list-group-item list-group-item-danger"
        >
          {todo}
        </motion.li>
      ))}
    </ul>
  </div>
);
export const ToggleContent = ({ isVisible }) => (
  <AnimatePresence>
    {isVisible && (
      <motion.div 
        initial={{ height: 0, opacity: 0 }}
        animate={{ height: 'auto', opacity: 1 }}
        exit={{ height: 0, opacity: 0 }}
        className="alert alert-dark mt-2"
      >
        This content is now visible!
      </motion.div>
    )}
  </AnimatePresence>
);