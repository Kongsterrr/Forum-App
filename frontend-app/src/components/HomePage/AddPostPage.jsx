import React, { useState }  from 'react';

function AddPostPage({ open, onClose, fetchPosts }) {
  if (!open) return null;

  const [postData, setPostData] = useState({
    title: "",
    content: "",
    isArchived: false,
    status: "Published"
    });
    const [profileImage, setProfileImage] = useState('');


    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setPostData({ ...postData, [name]: value });
    };

    const handleFileChange = (event) => {
      const file = event.target.files[0];
      const imageUrl = URL.createObjectURL(file);
      const reader = new FileReader();
      reader.onload = () => {
          let fileData = reader.result;
          fileData = fileData.split(',')[1];

          setProfileImage({ file_path: imageUrl, file_object: fileData });
      };
      reader.readAsDataURL(file);
    };

  const handleSubmit = async () => {
    try {
        const finalPostData = { ...postData };
        if (profileImage) {
          finalPostData.images = [profileImage];
        }
        console.log(finalPostData);
        const response = await fetch("http://127.0.0.1:5000/post_and_reply/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            },
            body: JSON.stringify(finalPostData)
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
                <div>
                  <input
                    type="file"
                    accept="image/*"
                    onChange={handleFileChange}
                  />
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