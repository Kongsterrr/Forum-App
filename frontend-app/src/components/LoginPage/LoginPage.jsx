import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { useSelector } from 'react-redux';

import { setUserLoginData } from '../../store/actions/LoginActions';
import { jwtDecode } from "jwt-decode";
import LoginForm from './LoginForm';

function LoginPage() {
  const dispatch = useDispatch();
  const userStatus = useSelector(state => state.userLogin.userStatus);
  const navigate = useNavigate();

  useEffect(() => {
    console.log("User status changed:", userStatus);
  }, [userStatus]);

  const handleLogin = (token) => {
    localStorage.setItem('token', token);
    console.log('User logged in successfully');
    const decodedToken = jwtDecode(token);
    const user_status = decodedToken.user_status; 
    const user_id = decodedToken.user_id; 


    dispatch(setUserLoginData(user_status, user_id))

    // Redirect the user based on user_status
    if (user_status === 'Normal') {
      navigate('/email-verify');
    } 
    else if (user_status === 'SuperAdmin' || user_status === 'Admin') {
      navigate('/admin');
    } 
    else {
      navigate('/user-profile');
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
