import React from 'react';

const MessageRow = ({ message, onToggleStatus }) => {
    const { dateCreated, email, message: msg, status } = message;

    return (
        <tr>
            <td>{dateCreated}</td>
            <td>{email}</td>
            <td>{msg}</td>
            <td>
                <MessageStatusButton status={status} onToggle={() => onToggleStatus(message)} />
            </td>
        </tr>
    );
};

export default MessageRow;
