import React from "react";
import { AppProvider } from "./context/AppContext";
import UserProfile from "./components/UserProfile";
import Dashboard from "./components/Dashboard";
import ErrorBoundary from "./components/ErrorBoundary";
import ErrorComponent from "./components/ErrorComponent";
import withLoader from "./hoc/withLoader";
const DashboardWithLoader = withLoader(Dashboard);
function App() {
  return (
    <AppProvider>
      <div className="container mt-4">
        <h1 className="text-center">React Advanced Patterns Demo</h1>

        <UserProfile />

        <DashboardWithLoader isLoading={false} />

        <ErrorBoundary>
          <ErrorComponent />
        </ErrorBoundary>
      </div>
    </AppProvider>
  );
}
export default App;