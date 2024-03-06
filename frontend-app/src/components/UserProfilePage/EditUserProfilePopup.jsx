import React, { useState } from 'react';

function EditProfilePopup({ onClose, onSave }) {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [profileImage, setProfileImage] = useState('');
  
  const handleSave = () => {
    onSave({ firstName, lastName, email, profileImage });
    onClose();
  };

  const handleClose = () => {
    onClose();
  };


  return (
    <div>
      <h2>Edit Profile</h2>
      <div>
        <label htmlFor="firstName">First Name:</label>
        <input
          type="text"
          id="firstName"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="lastName">Last Name:</label>
        <input
          type="text"
          id="lastName"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="profileImage">Profile Image URL:</label>
        <input
          type="text"
          id="profileImage"
          value={profileImage}
          onChange={(e) => setProfileImage(e.target.value)}
        />
      </div>
      <div>
        <button onClick={handleSave}>Save</button>
        <button onClick={handleClose}>Cancel</button>
      </div>
    </div>
  );
}

export default EditProfilePopup;
