export const FETCH_USERS_SUCCESS = 'FETCH_USERS_SUCCESS';
export const FETCH_USERS_FAILURE = 'FETCH_USERS_FAILURE';
export const UPDATE_USER_STATUS_SUCCESS = 'UPDATE_USER_STATUS_SUCCESS';
export const UPDATE_USER_STATUS_FAILURE = 'UPDATE_USER_STATUS_FAILURE';


// localStorage.setItem('token', 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5LCJ1c2VyX3N0YXR1cyI6IkFkbWluIiwiZXhwIjoxNzEwMTg5MDgyfQ.GasMqXCzG0iltZ0PvA_0prpi4K5Yo_PEeIBBCk-WO4U');

const token = localStorage.getItem('token');

export const fetchUsers = () => async (dispatch) => {
    try {
      const response = await fetch('http://127.0.0.1:5000/users/all', {
        headers: {
          'Authorization': `${token}`
        }
      });
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error);
      }

      const data = await response.json();

      dispatch({type: FETCH_USERS_SUCCESS, payload: data})

    } catch (error) {
      console.log("I am here")
      dispatch({type: FETCH_USERS_FAILURE, payload: error})

    }
  };

const updateUserStatus = async (dispatch, userId, actionType, newStatus) => {
  try {
    const endpoint = `http://127.0.0.1:5000/users/${actionType}/${userId}`;
    await fetch(endpoint, {
      method: 'PUT',
      headers: { 'Authorization': `${token}` }
    });
    dispatch({
      type: UPDATE_USER_STATUS_SUCCESS,
      payload: { userId, newStatus }
    });
  } catch (error) {
    dispatch({ type: UPDATE_USER_STATUS_FAILURE, payload: error });
  }
};

export const banUser = (userId) => (dispatch) => updateUserStatus(dispatch, userId, 'ban', 'banned');
export const unbanUser = (userId) => (dispatch) => updateUserStatus(dispatch, userId, 'unban', 'unbanned');
