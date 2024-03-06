const initialState = {
    responseMessage: '',
};

const contactReducer = (state = initialState, action) => {
    switch (action.type) {
        case 'SET_RESPONSE_MESSAGE':
            return { ...state, responseMessage: action.payload };
        default:
            return state;
    }
};

export default contactReducer;
