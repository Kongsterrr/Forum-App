export const setUserStatus = (status) => ({
  type: 'SET_USER_STATUS',
  payload: status,
});

export const setUserId = (user_id) => ({
  type: 'SET_USER_ID',
  payload: user_id,
});

export const setUserFirstname = (firstName) => ({
  type: 'SET_USER_FIRSTNAME',
  payload: firstName,
});

export const setUserLastname = (lastName) => ({
  type: 'SET_USER_LASTNAME',
  payload: lastName,
});

export const setUserEmail = (email) => ({
  type: 'SET_USER_EMAIL',
  payload: email,
});

export const setUserPic = (profileImageURL) => ({
  type: 'SET_USER_PIC',
  payload: profileImageURL,
});

export const setUserLoginData = (userStatus, userId) => {
  return {
    type: 'SET_USER_LOGIN_DATA',
    payload: { userStatus, userId },
  };
};

export const setUserProfileData = (profileData) => {
  return {
    type: 'SET_USER_PROFILE_DATA',
    payload: profileData,
  };
};
