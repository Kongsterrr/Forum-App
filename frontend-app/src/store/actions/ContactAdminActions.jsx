// const hardcoded_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX3N0YXR1cyI6IkFkbWlubiIsImV4cCI6MTcwOTc2NjE0N30.ZaWKX01NcNPJ1A_TK6LrTTVVJKy2HC1S7DMgZeTRKEk"

export const submitMessage = formData => async dispatch => {
    try {
        const response = await fetch('http://127.0.0.1:5000/messages/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${localStorage.getItem('token')}`,
                // Authorization: `Bearer ${hardcoded_token}`,
            },
            body: JSON.stringify(formData),
        });
        const data = await response.json();
        dispatch({ type: 'SET_RESPONSE_MESSAGE', payload: data.message });
    } catch (error) {
        console.error('Error submitting message:', error);
    }
};
