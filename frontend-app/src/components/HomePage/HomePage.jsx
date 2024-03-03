import React, { useEffect } from "react";
import UserCard from "../UserCard/UserCard";
import { useState } from "react";
import PostCard from "../PostCard/PostCard";
// import CreatePostModal from "./CreatePostModal";

export default function HomePage() {
    
    let [allPosts, setAllPosts] = useState([])
    let [postItem, setPostItem] = useState([{
        title: "",
        first_name: "",
        last_name: "",
        date: "",
    }])
    const [showCreatePostModal, setShowCreatePostModal] = useState(false);


    const fetchPosts = async () => {
        const response = await fetch("http://127.0.0.1:5000/post-details/");
        const data = await response.json();
        const allPostsData = [];
        for (let i = 0; i < data.length; i++) {
            if ("title" in data[i] && "firstName" in data[i] && "lastName" in data[i] && "date" in data[i]) {
                allPostsData.push(data[i]);
            }
        }
        setAllPosts(allPostsData);
    }

    useEffect(() => {
        fetchPosts();
    }, []);

    const handleCreatePost = async (postData) => {
        try {
            const response = await fetch("http://127.0.0.1:5000/post_and_reply/", {
                method: "POST",
                headers: {
                    "Authorization": `Bearer ${localStorage.getItem("token")}`
                },
                body: JSON.stringify(postData)
            });
            if (!response.ok) {
                throw new Error("Failed to create post");
            }
            // fetchPosts();
            // setShowCreatePostModal(false);
        } catch (error) {
            console.error("Error creating post:", error);
        }
    };

    return (
        <div>
            <h1>Home Page</h1>
            <p>Welcome to the home page of the Forum App.</p>

            <button onClick={() => setShowCreatePostModal(true)}>Create Post</button>

            {showCreatePostModal && (
                <CreatePostModal onClose={() => setShowCreatePostModal(false)} onCreatePost={handleCreatePost} />
            )}

            <div>
                {allPosts.map((post, index) => (
                    <PostCard key={index} post={post} />
                ))}
            </div>
        </div>
    );
}

function CreatePostModal({ onClose, onCreatePost }) {
    const [postData, setPostData] = useState({
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

    const handleSubmit = () => {
        console.log(postData["title"]);
        console.log(postData["content"]);
        console.log(postData);
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