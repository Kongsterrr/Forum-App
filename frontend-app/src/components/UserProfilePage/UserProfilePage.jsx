import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector } from 'react-redux';

function UserProfilePage() {
  const history = useHistory();
  const user = useSelector(state => state.user); 
  const [profileImage, setProfileImage] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [registrationDate, setRegistrationDate] = useState('');

  const fetchUserData = async () => {
    try {
      const response = await fetch('API_ENDPOINT_HERE');
      if (!response.ok) {
        throw new Error('Failed to fetch user data');
      }
      const userData = await response.json();

      setProfileImage(userData.profileImage);
      setFirstName(userData.firstName);
      setLastName(userData.lastName);
      setRegistrationDate(userData.registrationDate);
    } catch (error) {
      console.error('Error fetching user data:', error);
    }
  };

  useEffect(() => {
    fetchUserData();
  }, []);

  const handleEditProfile = () => {
    history.push('/edit-profile');
  };

  return (
    <div>
      <h1>User Profile Page</h1>
      <div>
        <img src={profileImage} alt="Profile" />
      </div>
      <div>
        <p>First Name: {firstName}</p>
        <p>Last Name: {lastName}</p>
        <p>Registration Date: {registrationDate}</p>
      </div>
      <button onClick={handleEditProfile}>Edit Profile</button>
    </div>
  );
}

export default UserProfilePage;
