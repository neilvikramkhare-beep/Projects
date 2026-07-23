import React, { createContext, useState } from "react";
export const AppContext = createContext();
export const AppProvider = ({ children }) => {
  const [user, setUser] = useState("John Doe");
  const [theme, setTheme] = useState("light");
  const toggleTheme = () => {
    setTheme(theme === "light" ? "dark" : "light");
  };
  return (
    <AppContext.Provider value={{ user, setUser, theme, toggleTheme }}>
      {children}
    </AppContext.Provider>
  );
};