const initialState = {
    token: null,
    userStatus: null
  };
  
  const loginReducer = (state = initialState, action) => {
    switch (action.type) {
        case 'LOGIN_SUCCESS':
            return { ...state, token: action.payload, error: null };
        case 'LOGIN_FAILURE':
            return { ...state, error: action.payload };
        case 'LOGIN_USER':
            return {
            ...state,
            token: action.payload
            };
        case 'SET_USER_STATUS':
            return {
            ...state,
            userStatus: action.payload
            };
        default:
            return state;
    }
  };
  
  export default loginReducer;