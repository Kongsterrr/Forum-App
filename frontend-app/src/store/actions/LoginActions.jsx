export const login = (formData) => async (dispatch) => {
    try {
      const response = await fetch('http://127.0.0.1:5000/authentication/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });
  
      if (!response.ok) {
        throw new Error('Failed to log in');
      }
  
      const data = await response.json();
      dispatch({ type: 'LOGIN_SUCCESS', payload: data.token });
    } catch (error) {
      console.error('Failed to log in:', error);
      dispatch({ type: 'LOGIN_FAILURE', payload: error.message });
    }
  };

export const loginUser = (token) => ({
    type: 'LOGIN_USER',
    payload: token
  });
  
export const setUserStatus = (userStatus) => ({
type: 'SET_USER_STATUS',
payload: userStatus
});
  