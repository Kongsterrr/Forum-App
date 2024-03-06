import { FETCH_MESSAGES, TOGGLE_MESSAGE_STATUS } from '../actions/MessageManagementActions.jsx';

const MessageManagementReducer = (state = [], action) => {
    switch (action.type) {
        case FETCH_MESSAGES:
            return action.payload;
        case TOGGLE_MESSAGE_STATUS:
            return state.map(message =>
                message.messageId === action.payload.messageId
                    ? { ...message, status: action.payload.status }
                    : message
            );
        default:
            return state;
    }
};

export default MessageManagementReducer;

