import React, { useState, useEffect } from 'react';


function EditProfilePopup({ onClose, onSave, currentFirstName, currentLastName, currentEmail, currentProfileImage }) {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [profileImage, setProfileImage] = useState('');

  useEffect(() => {
    setFirstName(currentFirstName);
    setLastName(currentLastName);
    setEmail(currentEmail);
    setProfileImage(currentProfileImage);
  }, [currentFirstName, currentLastName, currentEmail, currentProfileImage]);
  
  const handleSave = () => {
    console.log({ firstName, lastName, email, profileImage })
    onSave({ firstName, lastName, email, profileImage });
    onClose();
  };

  const handleClose = () => {
    onClose();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    const imageUrl = URL.createObjectURL(file);
    const reader = new FileReader();
    reader.onload = () => {
        let fileData = reader.result;
        fileData = fileData.split(',')[1];
        setProfileImage({ file_path: imageUrl, file_object: fileData });
    };
    reader.readAsDataURL(file);
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
        <label htmlFor="profileImage">Profile Image:</label>
        <input
          type="file"
          id="profileImage"
          accept="image/*"
          onChange={handleFileChange}
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
