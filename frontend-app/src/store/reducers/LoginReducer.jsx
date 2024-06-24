import {LOGOUT} from "../actions/LogOutActions.jsx";

const initialState = {
    userStatus: null,
    userId: null,
    registrationDate: null,
    email: null,
    firstName: null,
    lastName: null,
    profileImageURL: null,
  };
  
  const loginReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'SET_USER_STATUS':
        return {
          ...state,
          userStatus: action.payload,
        };
      case 'SET_USER_ID':
        return {
          ...state,
          userId: action.payload,
        };
      case 'SET_USER_FIRSTNAME':
        return {
          ...state,
          firstName: action.payload,
        };
      case 'SET_USER_LASTNAME':
        return {
          ...state,
          lastName: action.payload,
        };
      case 'SET_USER_EMAIL':
        return {
            ...state,
            email: action.payload,
        };
      case 'SET_USER_PIC':
        return {
            ...state,
            profileImageURL: action.payload,
        };
      case 'SET_USER_LOGIN_DATA':
        return {
            ...state,
            userStatus: action.payload.userStatus,
            userId: action.payload.userId,
        };
      case 'SET_USER_PROFILE_DATA':
        return {
            ...state,
            firstName: action.payload.firstName,
            lastName: action.payload.lastName,
            email: action.payload.email,
            registrationDate: action.payload.registrationDate,
            profileImageURL: action.payload.profileImageURL,
        };
      case LOGOUT:
        return {
          ...initialState,
        };
      default:
        return state;
    }
  };
  
  export default loginReducer;
  