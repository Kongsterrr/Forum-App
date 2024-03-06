export const FETCH_MESSAGES = 'FETCH_MESSAGES';
export const TOGGLE_MESSAGE_STATUS = 'TOGGLE_MESSAGE_STATUS';

const hardcoded_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX3N0YXR1cyI6IkFkbWluIiwiZXhwIjoxNzA5NzY2MzMzfQ.LD9UqNp9zojPFBHtTIIGRXK96bNUYYh_BFG0lpb7SAs"

export const fetchMessages = () => dispatch => {

    fetch('http://127.0.0.1:5000/messages/', {
        headers: {
            // Authorization: `Bearer ${localStorage.getItem('token')}`,
            Authorization: `Bearer ${hardcoded_token}`,
        },
    })
        .then(response => response.json())
        .then(messages => {
            dispatch({
                type: FETCH_MESSAGES,
                payload: messages,
            });
        })
        .catch(error => console.error('Error fetching messages:', error));
};

export const toggleMessageStatus = (messageId, status) => dispatch => {
    fetch(`http://127.0.0.1:5000/messages/${messageId}?status=${status}`, {
        method: 'PATCH',
        headers: {
            // Authorization: `Bearer ${localStorage.getItem('token')}`,
            Authorization: `Bearer ${hardcoded_token}`,
        },
    })
        .then(response => response.json())
        .then(() => {
            dispatch({
                type: TOGGLE_MESSAGE_STATUS,
                payload: {
                    messageId,
                    status,
                },
            });
        })
        .catch(error => console.error('Error toggling message status:', error));
};
