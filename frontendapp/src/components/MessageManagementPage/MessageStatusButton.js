import React from 'react';

const MessageStatusButton = ({ status, onToggle }) => {
    return (
        <button onClick={onToggle}>
            {status === 'Open' ? 'Close' : 'Open'}
        </button>
    );
};

export default MessageStatusButton;
