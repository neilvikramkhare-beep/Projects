import React, { useState, StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
const styles = {
  app:
  {
    fontFamily: 'sans-serif',
    WebkitFontSmoothing: 'auto',
    MozFontSmoothing: 'auto',
    MozOsxFontSmoothing: 'grayscale',
    fontSmoothing: 'auto',
    textRendering: 'optimizeLegibility',
    fontSmooth: 'always',
    WebkitTapHighlightColor: 'transparent',
    WebkitTouchCallout: 'none',
    textAlign: 'center', 
    padding: '20px'
  },
  h1:
  {
    fontSize: '1.5rem',
  },
};
function App() 
{
  const [count, setCount] = useState(0);
  const handleClick = () => {
    setCount(count + 1);
  };
  return (
    <div style={styles.app}> {}
      <>
        <h1 style={styles.h1}>welcome to my first react app!</h1>
        <p>ClickCount: {count}</p>
        {}
        <button onClick={handleClick}>Increment Count</button>
      </>
    </div>
  );
}
const container = document.getElementById('root');
if (container) 
{
    const root = createRoot(container);
    root.render(
      <StrictMode>
        <App />
      </StrictMode>
    );
} 
else
{
    console.error("Root element with ID 'root' not found. Please add <div id='root'></div> to your HTML.");
}