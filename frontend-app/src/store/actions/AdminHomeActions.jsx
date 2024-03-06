export const FETCH_POSTS_SUCCESS = 'FETCH_POSTS_SUCCESS';
export const FETCH_POSTS_FAILURE = 'FETCH_POSTS_FAILURE';
export const UPDATE_POST_STATUS_SUCCESS = 'UPDATE_POST_STATUS_SUCCESS';
export const UPDATE_POST_STATUS_FAILURE = 'UPDATE_POST_STATUS_FAILURE';


// localStorage.setItem('token', 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5LCJ1c2VyX3N0YXR1cyI6IkFkbWluIiwiZXhwIjoxNzEwMTg5MDgyfQ.GasMqXCzG0iltZ0PvA_0prpi4K5Yo_PEeIBBCk-WO4U');

const token = localStorage.getItem('token');

export const fetchPosts = () => async (dispatch) => {
  try {
    const response = await fetch('http://127.0.0.1:5000/post-details/admin', {
      headers: {
        'Authorization': `${token}`
      }
    });
    const data = await response.json();
    dispatch({ type: FETCH_POSTS_SUCCESS, payload: data });
  } catch (error) {
    dispatch({ type: FETCH_POSTS_FAILURE, payload: error });
  }
};

const updatePostStatus = async (dispatch, postId, actionType, newStatus) => {
  try {
    const endpoint = `http://127.0.0.1:5000/post_and_reply/${postId}/${actionType}`;
    await fetch(endpoint, {
      method: 'PUT',
      headers: { 'Authorization': `${token}` }
    });
    dispatch({
      type: UPDATE_POST_STATUS_SUCCESS,
      payload: { postId, newStatus }
    });
  } catch (error) {
    dispatch({ type: UPDATE_POST_STATUS_FAILURE, payload: error });
  }
};

export const banPost = (postId) => (dispatch) => updatePostStatus(dispatch, postId, 'banned', 'banned');
export const unbanPost = (postId) => (dispatch) => updatePostStatus(dispatch, postId, 'unbanned', 'unbanned');
export const recoverPost = (postId) => (dispatch) => updatePostStatus(dispatch, postId, 'recoverDeleted', 'recoverDeleted');
