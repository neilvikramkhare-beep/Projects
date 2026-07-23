import React from 'react';
import styles from './AppLayout.module.css';
const AppLayout = ({ children }) => {
  return (
    <div className={styles.appContainer}>
      <header className={styles.header}>
        <h1 style={{ fontSize: '1.5rem', margin: 0 }}>React Dashboard</h1>
        <div className={styles.userProfile}>Developer Mode</div>
      </header>
      <main className={styles.mainContent}>
        {}
        {React.Children.map(children, child => (
          <div className={styles.card}>{child}</div>
        ))}
      </main>
    </div>
  );
};
export default AppLayout;