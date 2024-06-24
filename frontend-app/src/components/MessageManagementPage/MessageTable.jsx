// import React from 'react';
import PropTypes from "prop-types";

const MessageTable = ({ children }) => {
    return (
        <table>
            <thead>
            <tr>
                <th>Date Created</th>
                <th>Email</th>
                <th>Message</th>
                <th>Status</th>
            </tr>
            </thead>
            <tbody>
            {children}
            </tbody>
        </table>
    );
};

MessageTable.propTypes = {
    children: PropTypes.node.isRequired, // Validate that children is a React node and is required
};

export default MessageTable;