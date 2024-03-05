
import { FETCH_POSTS_SUCCESS, FETCH_POSTS_FAILURE, UPDATE_POST_STATUS_SUCCESS, UPDATE_POST_STATUS_FAILURE } from '../actions/AdminHomeActions';

const initialState = {
  postsData: {
    published_posts: [],
    banned_posts: [],
    deleted_posts: []
  },
  error: null
};

const findAndRemovePost = (state, postId) => {
  let postToRemove = null;

  ['published_posts', 'banned_posts', 'deleted_posts'].forEach((key) => {
    const index = state.postsData[key].findIndex(post => post.postId === postId);
    if (index > -1) {
      postToRemove = { ...state.postsData[key][index] };
      state.postsData[key].splice(index, 1);
    }
  });

  return { postToRemove };
};

const adminHomeReducer = (prevState = initialState, action) => {
  switch (action.type) {
    case FETCH_POSTS_SUCCESS:
      return {
        ...prevState,
        postsData: action.payload,
        error: null
      };
    case FETCH_POSTS_FAILURE:
      return {
        ...prevState,
        error: action.payload
      };
    case UPDATE_POST_STATUS_FAILURE:
      return {
        ...prevState,
        error: action.payload
      };

    case UPDATE_POST_STATUS_SUCCESS: {
      const {postId, newStatus} = action.payload;
      const newState = {...prevState, postsData: {...prevState.postsData}, error: null};
      const {postToRemove} = findAndRemovePost(newState, postId);

      if (!postToRemove) {
        console.error('Post not found:', postId);
        return prevState;
      }

      switch (newStatus) {
        case 'banned':
          newState.postsData.banned_posts.push(postToRemove);
          break;
        case 'unbanned':
          newState.postsData.published_posts.push(postToRemove);
          break;
        case 'recoverDeleted':
          newState.postsData.published_posts.push(postToRemove);
          break;
        default:
          console.error('Unhandled newStatus:', newStatus);
          return prevState;
      }

      return newState;
    }
    default:
      return prevState;
  }
};

export default adminHomeReducer;
