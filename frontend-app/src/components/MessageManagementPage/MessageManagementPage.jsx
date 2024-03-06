import { useEffect } from 'react';
// import MessageTable from './MessageTable';
// import MessageRow from './MessageRow';
import { connect } from 'react-redux';
import { fetchMessages, toggleMessageStatus } from '../../store/actions/MessageManagementActions.jsx';
import PropTypes from "prop-types";


const MessageManagementPage = ({ messages, fetchMessages, toggleMessageStatus }) => {
    useEffect(() => {
        fetchMessages();
    }, [fetchMessages]);

    const handleToggleStatus = (messageId, currentStatus) => {
        const newStatus = currentStatus === 'Open' ? 'Close' : 'Open';
        toggleMessageStatus(messageId, newStatus);
    };

    return (
        <div>
            <h1>Message Management</h1><br />
            <table>
                <thead>
                <tr>
                    <th className="px-4">Date Created</th>
                    <th className="px-4">Email</th>
                    <th className="px-4">Message</th>
                    <th className="px-4">Status</th>
                </tr>
                </thead>
                <tbody>
                {messages.map(message => (
                    <tr key={message.messageId}>
                        <td className="px-4">{message.dateCreated}</td>
                        <td className="px-4">{message.email}</td>
                        <td className="px-4">{message.message}</td>
                        <td className="px-4">
                            <button onClick={() => handleToggleStatus(message.messageId, message.status)} style={{ backgroundColor: message.status === 'Open' ? 'lightgrey' : 'darkgrey' }}>
                                {"Change to " + message.status}
                            </button>
                        </td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
};

MessageManagementPage.propTypes = {
    messages: PropTypes.array, // Validate messages prop
    fetchMessages: PropTypes.func.isRequired, // Validate fetchMessages prop
    toggleMessageStatus: PropTypes.func.isRequired, // Validate toggleMessageStatus prop
};

const mapStateToProps = state => ({
    messages: state.messages,
});

export default connect(mapStateToProps, {fetchMessages, toggleMessageStatus})(MessageManagementPage);


// const MessageManagementPage = () => {
//     const [messages, setMessages] = useState([]);
//
//     useEffect(() => {
//         fetchMessages();
//     }, []);
//
//     const hardcoded_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX3N0YXR1cyI6IkFkbWluIiwiZXhwIjoxNzA5NzQzMDY0fQ.0EC8_6z0RkZU6dbEuWx8yOriqHE0SfZ7D4D6EPjmhm4"
//
//     const fetchMessages = async () => {
//         // Fetch messages data from the provided URL
//         try {
//             const response = await fetch('http://127.0.0.1:5000/messages/', {
//                 headers: {
//                     // Authorization: `Bearer ${localStorage.getItem('token')}`,
//                     Authorization: `Bearer ${hardcoded_token}`,
//                 },
//             });
//
//
//             if (!response.ok) {
//                 throw new Error('Failed to fetch messages');
//             }
//
//             const data = await response.json();
//             setMessages(data);
//         } catch (error) {
//             console.error('Error fetching messages:', error.message);
//         }
//     };
//
//     const toggleStatus = async (message) => {
//         try {
//             const newStatus = message.status === 'Open' ? 'Close' : 'Open';
//             await fetch(`http://127.0.0.1:5000/messages/${message.messageId}?status=${newStatus}`, {
//                 method: 'PATCH',
//                 headers: {
//                     // Authorization: `Bearer ${localStorage.getItem('token')}`,
//                     Authorization: `Bearer ${hardcoded_token}`,
//                     'Content-Type': 'application/json',
//                 },
//             });
//             // Update the local state with the new status
//             setMessages(messages.map(m => {
//                 if (m.messageId === message.messageId) {
//                     return { ...m, status: newStatus };
//                 }
//                 return m;
//             }));
//         } catch (error) {
//             console.error('Error toggling status:', error);
//         }
//     };
//
//     return (
//         <div>
//             <h1>Message Management Page</h1>
//             <MessageTable>
//                 {messages.map(message => (
//                     <MessageRow key={message.messageId} message={message} onToggleStatus={() => toggleStatus(message)} />
//                 ))}
//             </MessageTable>
//         </div>
//     );
// };

// export default MessageManagementPage;
