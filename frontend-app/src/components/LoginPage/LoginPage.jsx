import React from 'react';
import LoginForm from './LoginForm';

function LoginPage() {
  const handleLogin = (token) => {
    localStorage.setItem('token', token);
    console.log('User logged in successfully');
    window.location.href = '/email-verify';
  };

  return (
    <div>
      <h1>Login Page</h1>
      <LoginForm onLogin={handleLogin} />
    </div>
  );
}

export default LoginPage;
