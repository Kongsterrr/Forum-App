import React, { useState } from 'react';

function AddReplyPage({ open, onClose, postId, fetchPost }) {
  if (!open) return null;

  const [replyData, setReplyData] = useState({
    comment: "",
    isActive: true
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setReplyData({ ...replyData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`http://127.0.0.1:5000/post_and_reply/${postId}/reply`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          // "Authorization": `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMCwidXNlcl9zdGF0dXMiOiJOb3JtYWwiLCJleHAiOjE3MTAyMTgzMzl9.W_cYS1IdKe4PoQ9eeo5MrBTMFGL-0E27FustfBTDFac`
          "Authorization": `Bearer ${localStorage.getItem("token")}`
        },
        body: JSON.stringify(replyData)
      });
      onClose();
      fetchPost(); // Fetch post again after successful submission to update replies
    } catch (error) {
      console.error("Error replying to post:", error);
    }
  };

  return (
    <div className='overlay'>
      <div className='modalContainer'>
        <div className='modalRight'>
          <p className='closeBtn' onClick={onClose}>
            X
          </p>
          <div className='content'>
            <h2>Reply to the Post</h2>
            <br></br>
            <form onSubmit={handleSubmit}>
              <div>
                <label>Comment:</label>
                <textarea name="comment" value={replyData.comment} onChange={handleInputChange} required />
              </div>
              <br></br>
              <button type="submit">Submit</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AddReplyPage;
