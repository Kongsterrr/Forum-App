// import React from 'react';
import PropTypes from 'prop-types';


const StatusButton = ({ status, onToggle }) => {
    return (
        <button
            onClick={onToggle}
            style={{ backgroundColor: status === 'Open' ? 'lightgrey' : 'darkgrey' }}
        >
            {status === 'Open' ? 'Change to Close' : 'Change to Open'}
        </button>
    );
};

// const StatusButton = ({ status, onToggle }) => {
//     return (
//         <button
//             onClick={onToggle}
//             style={{ backgroundColor: status === 'Open' ? 'lightgrey' : 'darkgrey' }}
//         >
//             {status === 'Open' ? 'Change to Close' : 'Change to Open'}
//         </button>
//     );
// };

StatusButton.propTypes = {
    status: PropTypes.string.isRequired, // Validate that status is a string and is required
    onToggle: PropTypes.func.isRequired, // Validate that onToggle is a function and is required
};

export default StatusButton;