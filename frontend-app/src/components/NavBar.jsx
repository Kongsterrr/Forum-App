// src/components/NavBar.jsx
import React from 'react';
import { NavLink} from 'react-router-dom';
import { Navbar, Nav, Container } from 'react-bootstrap';


const NavBar = ({ userGroup }) => {

  return (
    <Navbar expand="lg" className="bg-body-tertiary" fixed="top">
      <Container>
        <Navbar.Brand as={NavLink} to="/home">MyApp</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link as={NavLink} to="/home" end>Home</Nav.Link>

            {userGroup === 'admin' && (
              <>
                <Nav.Link as={NavLink} to="/admin" end>Admin</Nav.Link>
                <Nav.Link as={NavLink} to="/user-management" end>User Management</Nav.Link>
              </>
            )}

            {!userGroup && (
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
