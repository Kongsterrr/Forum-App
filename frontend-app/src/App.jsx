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
import NavBar from './components/NavBar';
import 'bootstrap/dist/css/bootstrap.min.css';
import MessageManagementPage from './components/MessageManagementPage/MessageManagementPage';
import UserProfilePage from './components/UserProfilePage/UserProfilePage.jsx';
import ProtectedRoute from './components/RouteGuard.jsx';
import DynamicRoute from './components/RouteForHome';

function App() {

  return (
      <Router>
          <NavBar/>

      <div className="main-content">
          <Routes>
              <Route path="/register" element={<RegisterPage/>}/>
              <Route path="/login" element={<LoginPage/>}/>

              <Route path="/home" element={<ProtectedRoute> <DynamicRoute /> </ProtectedRoute>}/>
              <Route path="/post/:postId" element={<ProtectedRoute> <PostDetailPage/>  </ProtectedRoute>}/>
              {/*<Route path="/admin" element={<ProtectedRoute> <AdminHomePage/>  </ProtectedRoute>}/>*/}
              <Route path="/user-management" element={<ProtectedRoute> <UserManagementPage/>  </ProtectedRoute>}/>

              <Route path="/email-verify" element={<EmailVerificationPage/>}/>
              <Route path="/user-profile" element={<ProtectedRoute> <UserProfilePage/>  </ProtectedRoute>}/>
              <Route path="/admin/messages" element={<ProtectedRoute> <MessageManagementPage />  </ProtectedRoute>} />
          </Routes>
      </div>

      </Router>

    )
}

export default App
