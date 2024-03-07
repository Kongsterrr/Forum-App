import React, { useState, useEffect } from 'react';
import PostCard from "../PostCard/PostCard";
import { Link, useNavigate } from 'react-router-dom';
import EditProfilePopup from './EditUserProfilePopup';
import { setUserId, setUserStatus, setUserFirstname, setUserLastname, setUserEmail, setUserPic, setUserProfileData } from '../../store/actions/LoginActions';
import { useDispatch } from 'react-redux';
import './UserProfile.css'
import { useSelector } from 'react-redux';

function UserProfilePage() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const [allHistoryPosts, setAllHistoryPosts] = useState([]);
    const [allDraftPosts, setAllDraftPosts] = useState([]);
    const firstName = useSelector(state => state.userLogin.firstName);
    const lastName = useSelector(state => state.userLogin.lastName);
    const registrationDate = useSelector(state => state.userLogin.registrationDate);
    const email = useSelector(state => state.userLogin.email);
    const profileImage = useSelector(state => state.userLogin.profileImageURL);

    const token = localStorage.getItem('token');
    const userStatus = useSelector(state => state.userLogin.userStatus);
    const userId = useSelector(state => state.userLogin.userId);
    const default_url = 'https://forum-app-bucket.s3.amazonaws.com/125-6cc93f1a-e574-4be3-b34d-4dcd0f45aad9.png?AWSAccessKeyId=AKIARKHNNC2NKDD7YEUY&Signature=be6PVSTKbCHfr5ilZNkvMbYzgWg%3D&Expires=1741322810';

    const [isModalOpen, setIsModalOpen] = useState(false);

    const openModal = () => {
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
    };

    const handleSave = (updatedUserData) => {
        console.log('Updated user data:', updatedUserData);
        // Handle unchanged data
        const changedUserData = {};

        if (updatedUserData.firstName !== firstName){
          changedUserData['firstName'] = updatedUserData.firstName
          dispatch(setUserFirstname(updatedUserData.firstName));
        }
        if (updatedUserData.lastName !== lastName){
          changedUserData['lastName'] = updatedUserData.lastName
          dispatch(setUserLastname(updatedUserData.lastName));
        }
        if (updatedUserData.email !== email){
          changedUserData['email'] = updatedUserData.email
          // Email changed, need to update user status in redux store
          dispatch(setUserStatus('Normal'));
          dispatch(setUserEmail(updatedUserData.email));
        }
        if (updatedUserData.profileImage !== profileImage){
          changedUserData['profileImage'] = updatedUserData.profileImage
          dispatch(setUserPic(updatedUserData.profileImage['file_path']));
        }
        
        console.log('Changed user data:', changedUserData);

        if (Object.keys(changedUserData).length > 0) {
          submitProfileData(changedUserData);
        } else {
          console.log('No changes detected');
        }
      };

    
    const submitProfileData = async (updatedUserData) => {
      try {
          const response = await fetch('http://127.0.0.1:5000/users/profile-update', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
                  'Authorization': `Bearer ${token}`
              },
              body: JSON.stringify(updatedUserData)
              });
      if (!response.ok) {
          throw new Error('Failed to update profile data');
      }
      } catch (error) {
      console.error('Error updating profile data:', error);
      }
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

        const formattedUserData = {
          registrationDate: userData.dateJoined,
          email: userData.email,
          firstName: userData.firstName,
          lastName: userData.lastName,
          profileImageURL: userData.profileImageURL || default_url,
        };

        // Update the data in redux store
        dispatch(setUserProfileData(formattedUserData));
        
        } catch (error) {
        console.error('Error fetching user data:', error);
        }
    };

    const fetchHistory = async () => {
      try {
          const response = await fetch('http://127.0.0.1:5000/post_history/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            });
          if (!response.ok) {
              throw new Error('Failed to fetch user data');
          }
          const data = await response.json();
          const post_history = data['post_history']
          console.log(post_history)
          setAllHistoryPosts(post_history);
      } catch (error) {
          console.error("Error fetching posts:", error);
      }
  };

    const fetchDrafts = async () => {
      try {
          const response = await fetch('http://127.0.0.1:5000/post_and_reply/drafts', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            });
          if (!response.ok) {
              throw new Error('Failed to fetch user data');
          }
          const data = await response.json();
          setAllDraftPosts(data);
      } catch (error) {
          console.error("Error fetching posts:", error);
      }
    };

    useEffect(() => {
        fetchUserData();
        fetchHistory();
        fetchDrafts();
    }, []);

    const handleVerifyNow = () => {
      if (userStatus === 'Normal') {
        // Redirect to email verification page
         navigate('/email-verify');
      }
    };

  return (
    <div>
      <section className="profile-section">
        <div>
          <img src={profileImage} alt="Profile" />
        </div>
        <div>
          <p>First Name: {firstName}</p>
          <p>Last Name: {lastName}</p>
          <p>Email: {email}</p>
          <p>Registration Date: {registrationDate}</p>
          <p>
            User Status: 
            {(userStatus === 'Normal' || userStatus === 'Normal-write') && (
              <button onClick={handleVerifyNow} disabled={userStatus === 'Normal-write'}>
                {userStatus === 'Normal' ? 'Verify Now' : 'Verified'}
              </button>
            )}
          </p>
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
      </section>

      <section className="history-section">
        <h2>Browsing History</h2>
        <ul>
          {allHistoryPosts.map((post, index) => (
            <Link to={`/post/${post.postId}`} key={index}>
              <PostCard post={post} />
            </Link>
          ))}
        </ul>
      </section>

      <section>
        <h2>Drafts</h2>
        <ul>
          {allDraftPosts.map((post, index) => (
            <Link to={`/post/${post.postId}`} key={index}>
              <PostCard post={post} />
            </Link>
          ))}
        </ul>
      </section>
    </div>
  );
}

export default UserProfilePage;
