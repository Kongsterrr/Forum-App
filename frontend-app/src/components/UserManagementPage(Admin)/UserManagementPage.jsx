import React, { useEffect, useState } from 'react';

export default function AdminHomePage() {
  const [usersData, setUsersData] = useState([]);

  // for testing purpose
  localStorage.setItem('token', 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5LCJ1c2VyX3N0YXR1cyI6IkFkbWluIiwiZXhwIjoxNzEwMDExOTAzfQ.qk3KkZHajW1ip915L7ExHyVj7wLbq8D-X1QdesruUxk');

  const fetchUsersData = async () => {
    const token = localStorage.getItem('token');
    try {
      const response = await fetch('http://127.0.0.1:5000/users/all', {
        headers: {
          'Authorization': `${token}`
        }
      });
      const data = await response.json();
      setUsersData(data);
    } catch (error) {
      console.error('Failed to fetch posts data:', error);
    }
  };

  useEffect(() => {
    fetchUsersData();
  }, []);

  return (
      <div>
          <h1>User Management</h1>
          <table>
              <thead>
              <tr>
                  <th>User ID</th>
                  <th>Full Name</th>
                  <th>Email</th>
                  <th>Date Joined</th>
                  <th>Type</th>
              </tr>
              </thead>
              <tbody>
              {usersData.map((user) => (
                  <tr key={user.userId}>
                      <td>{user.userId}</td>
                      <td>{`${user.firstName} ${user.lastName}`}</td>
                      <td>{user.email}</td>
                      <td>{user.dateJoined}</td>
                      <td>{user.type}</td>
                  </tr>
              ))}
              </tbody>
          </table>
      </div>
  );
}
