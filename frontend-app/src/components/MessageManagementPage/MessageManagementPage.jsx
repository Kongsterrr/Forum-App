import { useState, useEffect } from 'react';
import MessageTable from './MessageTable';
import MessageRow from './MessageRow';

const MessageManagementPage = () => {
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        fetchMessages();
    }, []);

    const hardcoded_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX3N0YXR1cyI6IkFkbWluIiwiZXhwIjoxNzA5NTgxMDkyfQ.VQcjvnfJLdXfFmK8Ba05BOigf0J8DlfkRHEooM2MQLc"

    const fetchMessages = async () => {
        // Fetch messages data from the provided URL
        try {
            const response = await fetch('http://127.0.0.1:5000/messages/', {
                headers: {
                    // Authorization: `Bearer ${localStorage.getItem('token')}`,
                    Authorization: `Bearer ${hardcoded_token}`,
                },
            });


            if (!response.ok) {
                throw new Error('Failed to fetch messages');
            }

            const data = await response.json();
            setMessages(data);
        } catch (error) {
            console.error('Error fetching messages:', error.message);
        }
    };

    const toggleStatus = async (message) => {
        try {
            const newStatus = message.status === 'Open' ? 'Close' : 'Open';
            await fetch(`http://127.0.0.1:5000/messages/${message.messageId}?status=${newStatus}`, {
                method: 'PATCH',
                headers: {
                    // Authorization: `Bearer ${localStorage.getItem('token')}`,
                    Authorization: `Bearer ${hardcoded_token}`,
                    'Content-Type': 'application/json',
                },
            });
            // Update the local state with the new status
            setMessages(messages.map(m => {
                if (m.messageId === message.messageId) {
                    return { ...m, status: newStatus };
                }
                return m;
            }));
        } catch (error) {
            console.error('Error toggling status:', error);
        }
    };

    return (
        <div>
            <h1>Message Management Page</h1>
            <MessageTable>
                {messages.map(message => (
                    <MessageRow key={message.messageId} message={message} onToggleStatus={() => toggleStatus(message)} />
                ))}
            </MessageTable>
        </div>
    );
};

export default MessageManagementPage;
