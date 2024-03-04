// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import React from 'react'
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./components/HomePage/HomePage";
import PostDetailPage from "./components/PostDetailPage/PostDetailPage";
import AdminHomePage from "./components/HomePage(Admin)/AdminHomePage.jsx";
import UserManagementPage from "./components/UserManagementPage(Admin)/UserManagementPage.jsx";
import RegisterPage from './components/RegisterPage/RegisterPage.jsx';
import LoginPage from './components/LoginPage/LoginPage.jsx';
import EmailVerificationPage from './components/EmailVerificationPage/EmailVerificationPage.jsx';




function App() {

  return (
    <Router>
      <Routes>
          <Route path="/home" element={<HomePage/>} />
          <Route path="/post/:postId" element={<PostDetailPage/>} />
          <Route path="/admin" element={<AdminHomePage/>} />
          <Route path="/user-management" element={<UserManagementPage/>} />
          <Route path="/register" element={<RegisterPage/>} />
          <Route path="/login" element={<LoginPage/>} />
          <Route path="/email-verify" element={<EmailVerificationPage/>} />
      </Routes>
    </Router>
  )
}

export default App
