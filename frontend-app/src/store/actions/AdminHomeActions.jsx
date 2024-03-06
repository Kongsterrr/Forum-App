export const FETCH_POSTS_SUCCESS = 'FETCH_POSTS_SUCCESS';
export const FETCH_POSTS_FAILURE = 'FETCH_POSTS_FAILURE';
export const UPDATE_POST_STATUS_SUCCESS = 'UPDATE_POST_STATUS_SUCCESS';
export const UPDATE_POST_STATUS_FAILURE = 'UPDATE_POST_STATUS_FAILURE';



export const fetchPosts = () => async (dispatch) => {

  const token = localStorage.getItem('token');

  try {
    const response = await fetch('http://127.0.0.1:5000/post-details/admin', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error);
    }

    const data = await response.json();

    dispatch({ type: FETCH_POSTS_SUCCESS, payload: data });

  } catch (error) {
    console.log("I am here")
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
