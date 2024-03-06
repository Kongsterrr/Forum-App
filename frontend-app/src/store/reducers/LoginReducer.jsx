const initialState = {
    userStatus: null,
    userId: null
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
          userId: action.payload
        };
      default:
        return state;
    }
  };
  
  export default loginReducer;
  