// import React from 'react';
import StatusButton from "./StatusButton.jsx";
import PropTypes from "prop-types";

const MessageRow = ({ message, onToggleStatus }) => {
    const { dateCreated, email, message: msg, status } = message;

    return (
        <tr>
            <td>{dateCreated}</td>
            <td>{email}</td>
            <td>{msg}</td>
            <td>
                <StatusButton status={status} onToggle={() => onToggleStatus(message)} />
            </td>
        </tr>
    );
};

MessageRow.propTypes = {
    message: PropTypes.shape({
        dateCreated: PropTypes.string.isRequired,
        email: PropTypes.string.isRequired,
        message: PropTypes.string.isRequired,
        status: PropTypes.string.isRequired,
    }).isRequired, // Validate that message is an object with specific shape and is required
    onToggleStatus: PropTypes.func.isRequired, // Validate that onToggleStatus is a function and is required
};
export default MessageRow;