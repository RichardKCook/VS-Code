import React from 'react';

const Dashboard = ({ user }) => {
  return (
    <div>
      <h1>Welcome, {user.username}!</h1>
      <p>This is your dashboard.</p>
      {/* Add more dashboard functionality here */}
    </div>
  );
};

export default Dashboard;
