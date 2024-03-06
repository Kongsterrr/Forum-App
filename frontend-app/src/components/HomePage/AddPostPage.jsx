import React, { useState }  from 'react';

function AddPostPage({ open, onClose, fetchPosts }) {
  if (!open) return null;

  const [postData, setPostData] = useState({
    title: "",
    content: "",
    isArchived: false,
    status: "Published"
    });

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setPostData({ ...postData, [name]: value });
    };

  const handleSubmit = async () => {
    try {
        const response = await fetch("http://127.0.0.1:5000/post_and_reply/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                // "Authorization": `Bearer ${localStorage.getItem("token")}`
                "Authorization": `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjYsInVzZXJfc3RhdHVzIjoiTm9ybWFsIiwiZXhwIjoxNzEwMjE3MzM4fQ.xBuCnpCKDrg0eVa4CdoRcoreBqw0aoNebR6tS0yNdjc`
            },
            body: JSON.stringify(postData)
        });
        onClose();
        fetchPosts();
    } catch (error) {
        console.error("Error creating post:", error);
    }
  };

  const handleSaveDraft = async () => {
    setPostData({ ...postData, status: "Unpublished" });
    postData.status = "Unpublished";
    handleSubmit();
  };

  return (
    <div className='overlay'>
      <div className='modalContainer'>
        <div className='modalRight'>
          <p className='closeBtn' onClick={onClose}>
            X
          </p>
          <div className='content'>
            <h2>Create a Post</h2>            
            <br></br>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Title:</label>
                    <input type="text" name="title" value={postData.title} onChange={handleInputChange} required />
                </div>
                <div>
                    <label>Content:</label>
                    <textarea name="content" value={postData.content} onChange={handleInputChange} required />
                </div>
                <br></br>
                <button type="submit">Submit</button>
                <button type="button" onClick={handleSaveDraft}>Save Draft</button>

            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AddPostPage;