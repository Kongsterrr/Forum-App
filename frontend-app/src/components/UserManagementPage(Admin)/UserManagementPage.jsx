import React, { useEffect, useState } from 'react';

export default function AdminHomePage() {
  const [usersData, setUsersData] = useState([]);

  // for testing purpose
  localStorage.setItem('token', 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5LCJ1c2VyX3N0YXR1cyI6IkFkbWluIiwiZXhwIjoxNzEwMDExOTAzfQ.qk3KkZHajW1ip915L7ExHyVj7wLbq8D-X1QdesruUxk');

  const token = localStorage.getItem('token');

  const fetchUsersData = async () => {
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

  const handleBan = async (userId) => {
    try {
      await fetch(`http://127.0.0.1:5000/users/ban/${userId}`, {
        method: 'PUT',
        headers: { 'Authorization': `${token}` }
      });
      fetchUsersData();
    } catch (error) {
      console.error('Failed to ban user:', error);
    }
  };

  const handleUnban = async (userId) => {
    try {
      await fetch(`http://127.0.0.1:5000/users/unban/${userId}`, {
        method: 'PUT',
        headers: { 'Authorization': `${token}` }
      });
      fetchUsersData();
    } catch (error) {
      console.error('Failed to unban user:', error);
    }
  };



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
                  <th>Status</th>
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
                      <td>
                          {user.type !== 'Admin' && user.type !== 'SuperAdmin' &&( // Assuming 'type' field indicates if a user is an admin
                              user.active === true ? (
                                  <button onClick={() => handleBan(user.userId)}>Ban</button>
                              ) : (
                                  <button onClick={() => handleUnban(user.userId)}>Unban</button>
                              )
                          )}
                      </td>
                  </tr>
              ))}
              </tbody>
          </table>
      </div>
  );
}
