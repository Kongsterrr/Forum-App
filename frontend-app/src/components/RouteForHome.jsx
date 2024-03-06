import React from 'react';
import { useSelector } from 'react-redux';
import HomePage from '../components/HomePage/HomePage';
import AdminHomePage from '../components/HomePage(Admin)/AdminHomePage';

const DynamicRoute = () => {
  const userStatus = useSelector((state) => state.userLogin.userStatus);

  if (userStatus === 'Admin') {
    return <AdminHomePage />;
  } else {
    return <HomePage />;
  }
};

export default DynamicRoute;
