import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { jwtDecode } from "jwt-decode";
import LoginForm from './LoginForm';

function LoginPage() {
  const handleLogin = (token) => {
    localStorage.setItem('token', token);
    console.log('User logged in successfully');
    const decodedToken = jwtDecode(token);
    const user_status = decodedToken.user_status; 
    console.log('decodedToken: ', decodedToken)
    console.log('user_status: ', user_status)

    // Redirect the user based on user_status
    if (user_status === 'Normal') {
      window.location.href = '/email-verify';
    } 
    else if (user_status === 'SuperAdmin' || user_status === 'Admin') {
      window.location.href = '/admin';
    } 
    else {
      window.location.href = '/home';
    }
  };

  return (
    <div>
      <h1>Login Page</h1>
      <LoginForm onLogin={handleLogin} />
      <p>First-timer? <Link to="/register">Click here to register!</Link></p>
    </div>
  );
}

export default LoginPage;
