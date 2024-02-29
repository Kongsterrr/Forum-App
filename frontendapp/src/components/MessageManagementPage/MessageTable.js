import React from 'react';

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

export default MessageTable;
