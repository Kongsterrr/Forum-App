import React from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { submitMessage } from '../../store/actions/ContactAdminActions';
import { useNavigate } from 'react-router-dom';

const ContactAdminPage = ({ submitMessage, responseMessage }) => {
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = {
            email: e.target.email.value,
            message: e.target.message.value
        };

        // Dispatch action to send message
        await submitMessage(formData);
        alert('Message saved successfully.');
        navigate('/user-profile');
    };

    return (
        <div>
            <h2>Contact Admin</h2>
            {responseMessage && <p>{responseMessage}</p>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="subject">Subject:</label>
                    <input
                        id="subject"
                        required
                    />
                </div>
                <div>
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        required
                    />
                </div>
                <div>
                    <label htmlFor="message">Message:</label>
                    <textarea
                        id="message"
                        required
                    ></textarea>
                </div>
                <button type="submit">Submit</button>
            </form>
        </div>
    );
};

ContactAdminPage.propTypes = {
    submitMessage: PropTypes.func.isRequired,
    responseMessage: PropTypes.string
};

const mapStateToProps = state => ({
    responseMessage: state.messages.responseMessage // assuming reducer sets the responseMessage in the state
});

export default connect(mapStateToProps, { submitMessage })(ContactAdminPage);
