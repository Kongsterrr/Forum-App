import React, { useState, useEffect } from 'react';
import EditProfilePopup from './EditUserProfilePopup';
import './UserProfile.css'
// import { useHistory } from 'react-router-dom';
import { useSelector } from 'react-redux';

function UserProfilePage() {
    // const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [profileImage, setProfileImage] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [registrationDate, setRegistrationDate] = useState('');
    const [email, setEmail] = useState('');
    const token = localStorage.getItem('token');
    const userStatus = useSelector(state => state.userLogin.userStatus);
    const userId = useSelector(state => state.userLogin.userId);
    const default_url = '';
    

    const [isModalOpen, setIsModalOpen] = useState(false);

    const openModal = () => {
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
    };

    const handleSave = (updatedUserData) => {
        console.log('Updated user data:', updatedUserData);
      };
    
    const fetchUserData = async () => {
        console.log('user profile token:', token)
        try {
            const response = await fetch('http://127.0.0.1:5000/users/' + userId, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
                });
        if (!response.ok) {
            throw new Error('Failed to fetch user data');
        }
        const userData = await response.json();

        console.log(userData)


        // Check if profile image present, if not, default pic
        if (userData.profileImageURL === null){
            // use default url
            setProfileImage(default_url)
        }
        else{
            setProfileImage(userData.profileImageURL)
        }
        
        setFirstName(userData.firstName);
        setLastName(userData.lastName);
        setRegistrationDate(userData.dateJoined);
        setEmail(userData.email)
        } catch (error) {
        console.error('Error fetching user data:', error);
        }
    };

    useEffect(() => {
        fetchUserData();
    }, []);

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
        <p>User Status: {userStatus}</p>
      </div>
      <button onClick={openModal}>Edit Profile</button>
      {isModalOpen && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={closeModal}>&times;</span>
            <EditProfilePopup 
              onSave={handleSave} 
              onClose={closeModal}
              currentFirstName={firstName}
              currentLastName={lastName}
              currentEmail={email}
              currentProfileImage={profileImage}
            />
          </div>
        </div>
      )}
    </div>
  );
}

export default UserProfilePage;
