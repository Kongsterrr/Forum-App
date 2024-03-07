import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';

function EmailVerificationForm() {
  const [verificationCode, setVerificationCode] = useState('');
  const [isCodeSent, setIsCodeSent] = useState(false);
  const [resendDisabled, setResendDisabled] = useState(false);
  const [countdown, setCountdown] = useState(60); 
  const token = localStorage.getItem('token');
  const navigate = useNavigate();
  let timer;

  useEffect(() => {
    console.log(token)
    if (!isCodeSent) {
      sendVerificationCode();
      setResendDisabled(true); 
    }
  }, []);

  useEffect(() => {
    if (countdown > 0) {
      timer = setTimeout(() => setCountdown(countdown - 1), 1000);
    } else {
      setResendDisabled(false);
    }
    return () => clearTimeout(timer);
  }, [countdown]); 

  const handleChange = (e) => {
    setVerificationCode(e.target.value);
  };

  const handleResendCode = () => {
    sendVerificationCode();
    setResendDisabled(true); 
    setCountdown(60); 
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
      if (data == true) {
        navigate('/home');
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
        <button type="button" onClick={handleResendCode} disabled={resendDisabled}>Resend Code</button>
        <p>Resend email in {countdown} seconds...</p>
      </form>
      <button onClick={handleLaterVerification}>Verify Later</button>
    </div>
  );
}

export default EmailVerificationForm;
