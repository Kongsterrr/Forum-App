// src/components/NavBar.jsx
import React from 'react';
import {NavLink, useNavigate} from 'react-router-dom';
import { Navbar, Nav, Container } from 'react-bootstrap';
import {useDispatch, useSelector} from 'react-redux';
import {logout} from "../store/actions/LogOutActions.jsx";



const NavBar = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user_status = useSelector(state => state.userLogin.userStatus);

  const handleLogout = () => {
    localStorage.removeItem('token');
    dispatch(logout());
    navigate('/login');
  };

  return (
    <Navbar expand="lg" className="bg-body-tertiary" fixed="top">
      <Container>
        <Navbar.Brand>MyApp</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            {user_status && (
              <>
                {user_status.includes('Normal') && (
                  <>
                    <Nav.Link as={NavLink} to="/home" end>Home</Nav.Link>
                    <Nav.Link as={NavLink} to="/user-profile" end>Profile</Nav.Link>
                  </>
                )}
                {user_status === 'Admin' && (
                  <>
                    <Nav.Link as={NavLink} to="/home" end>Admin</Nav.Link>
                    <Nav.Link as={NavLink} to="/user-management" end>User Management</Nav.Link>
                  </>
                )}
                <Nav.Link as="button" onClick={handleLogout}>Logout</Nav.Link>
              </>
            )}
            {user_status === null && (
              <>
                <Nav.Link as={NavLink} to="/login" end>Login</Nav.Link>
                <Nav.Link as={NavLink} to="/register" end>Register</Nav.Link>
              </>
            )}


          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar;
