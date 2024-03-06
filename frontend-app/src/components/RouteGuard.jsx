import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ children, requiredRoles= ['Admin', 'Normal', 'Normal-write']}) => {
  let hasRequiredRole = false
  const isAuthenticated = !!localStorage.getItem('token');
  const userStatus = localStorage.getItem('user_status')

  if (!isAuthenticated) {
    return <Navigate to="/login" />;
  }

  if (requiredRoles && requiredRoles.includes(userStatus)) {
    hasRequiredRole = true;
  }

  if (!hasRequiredRole) {
    return <Navigate to="/home" replace />;
  }

  return children;
};

export default ProtectedRoute;