import React from "react";
import { useState } from "react";

export default function CreatePostModal({ onClose, onCreatePost }) {
    const [postData, setPostData] = useState({
        userId: 5,
        title: "",
        content: "",
        isArchived: false,
        status: "Published"
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setPostData((prevData) => ({
            ...prevData,
            [name]: value
        }));
    };

    const handleSubmit = (e) => {
        console.log(postData["title"]);
        console.log(postData["content"]);
        onCreatePost(postData);
    };

    return (
        <div className="modal">
            <div className="modal-content">
                <span className="close" onClick={onClose}>&times;</span>
                <h2>Create Post</h2>
                <form onSubmit={handleSubmit}>
                    <label>
                        Title:
                        <input type="text" name="title" value={postData.title} onChange={handleChange} required />
                    </label>
                    <label>
                        Content:
                        <textarea name="content" value={postData.content} onChange={handleChange} required />
                    </label>
                    <button type="submit">Create</button>
                </form>
            </div>
        </div>
    );
}