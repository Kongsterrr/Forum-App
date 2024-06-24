import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import AddPostPage from "./AddPostPage";
import PostCard from "../PostCard/PostCard";
import "./AddPostPage.css";

export default function HomePage() {
    const [allPosts, setAllPosts] = useState([]);
    const [showAddPost, setShowAddPost] = useState(false);
    const [sortAscending, setSortAscending] = useState(true);


    useEffect(() => {
        console.log(localStorage.getItem("token"));
        fetchPosts();
    }, []);

    const fetchPosts = async () => {
        try {
            const response = await fetch("http://127.0.0.1:5000/post-details/");
            const data = await response.json();
            setAllPosts(data.filter(post => post.title && post.firstName && post.lastName && post.date));
        } catch (error) {
            console.error("Error fetching posts:", error);
        }
    };

    const toggleAddPost = () => {
        setShowAddPost(!showAddPost);
        console.log("showAddPost:", !showAddPost);

    };

    const handleSort = () => {
        const sortedPosts = [...allPosts].sort((a, b) => {
            const dateA = new Date(a.date);
            const dateB = new Date(b.date);
            return sortAscending ? dateA - dateB : dateB - dateA;
        });
        setAllPosts(sortedPosts);
        setSortAscending(!sortAscending);
    };

    return (
        <div>
            <h1>Home Page</h1>
            <p>Welcome to the home page of the Forum App.</p>

            <button onClick={toggleAddPost}>Create a Post</button>
            <button onClick={handleSort}>{sortAscending ? "Sort Ascending" : "Sort Descending"}</button>


            <AddPostPage open={showAddPost} onClose={toggleAddPost} fetchPosts={fetchPosts} />

            <div>
                {allPosts.map((post, index) => (
                    <Link to={`/post/${post.postId}`} key={index}>
                        <PostCard post={post} />
                    </Link>
                ))}
            </div>
        </div>
    );
}
