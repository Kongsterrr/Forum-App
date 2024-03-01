// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import React from 'react'
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./components/HomePage/HomePage";
import PostDetailPage from "./components/PostDetailPage/PostDetailPage";


function App() {

  return (
    <Router>
      <Routes>
          <Route path="/" element={<HomePage/>} />
          <Route path="/post/:postId" element={<PostDetailPage/>} />
      </Routes>
    </Router>
  )
}

export default App
