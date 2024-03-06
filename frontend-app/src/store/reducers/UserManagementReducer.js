// AdminHomeReducer.jsx
import { FETCH_USERS_SUCCESS, FETCH_USERS_FAILURE, UPDATE_USER_STATUS_SUCCESS, UPDATE_USER_STATUS_FAILURE } from '../actions/UserManagementActions';

const initialState = {
  usersData: [],
  error: null
};

const userManagementReducer = (prevState = initialState, action) => {
  switch (action.type) {
    case FETCH_USERS_SUCCESS:
      return {
        ...prevState,
        usersData: action.payload,
        error: null
      };
    case FETCH_USERS_FAILURE:
      return {
        ...prevState,
        error: action.payload
      };
    case UPDATE_USER_STATUS_FAILURE:
      return {
        ...prevState,
        error: action.payload
      };

    case UPDATE_USER_STATUS_SUCCESS: {
      const {userId, newStatus} = action.payload;
      const updatedUsersData = prevState.usersData.map(user => {
        if (user.userId === userId) {
          return { ...user, active: newStatus !== 'banned' };
        }
        return user;
      });
      return {
        ...prevState,
        usersData: updatedUsersData
      };

    }
    default:
      return prevState;
  }
};

export default userManagementReducer;
