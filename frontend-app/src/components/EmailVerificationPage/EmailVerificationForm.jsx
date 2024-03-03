import React, { useState, useEffect } from 'react';

function EmailVerificationForm() {
  const [verificationCode, setVerificationCode] = useState('');
  const [isCodeSent, setIsCodeSent] = useState(false);
  const token = localStorage.getItem('token');

  // Send verification to user email when the page initializes.
  useEffect(() => {
    if (!isCodeSent) {
      sendVerificationCode();
    }
  }, []);

  const handleChange = (e) => {
    setVerificationCode(e.target.value);
  };

  const handleResendCode = () => {
    sendVerificationCode();
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        const response = await fetch('http://127.0.0.1:5000/users/email', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          },
          body: JSON.stringify({
            'verification_code': verificationCode
          })
        });
  
        if (!response.ok) {
          throw new Error('Failed to authenticate the user.');
        }
  
        const data = await response.json();
        console.log(data)
        if(data==true){
            window.location.href = '/';
        }

      } catch (error) {
        console.error('Failed to log in:', error);
      }
    console.log('Verification code submitted:', verificationCode);
  };

  const sendVerificationCode = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/users/email', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
      });
  
      if (!response.ok) {
        throw new Error('Failed to send verification code');
      }

      setIsCodeSent(true);
    } catch (error) {
      console.error('Failed to send verification code:', error);
    }
  };

  const handleLaterVerification = () => {
    window.location.href = '/login'; 
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="verification_code">Verification Code:</label>
          <input
            type="text"
            id="verification_code"
            name="verification_code"
            value={verificationCode}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Submit</button>
        <button type="button" onClick={handleResendCode}>Resend Code</button>
      </form>
      <button onClick={handleLaterVerification}>Verify Later</button>
    </div>
  );
}

export default EmailVerificationForm;
