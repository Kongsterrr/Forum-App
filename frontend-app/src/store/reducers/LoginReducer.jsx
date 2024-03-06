const initialState = {
    userStatus: null,
  };
  
  const loginReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'SET_USER_STATUS':
        return {
          ...state,
          userStatus: action.payload,
        };
      default:
        return state;
    }
  };
  
  export default loginReducer;