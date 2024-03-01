import React, { useEffect } from "react";
import UserCard from "../UserCard/UserCard";
import { useState } from "react";
import PostCard from "../PostCard/PostCard";

export default function HomePage() {
    
    let [allPosts, setAllPosts] = useState([])
    let [postItem, setPostItem] = useState([{
        title: "",
        first_name: "",
        last_name: "",
        date: "",
    }])

    const fetchPosts = async () => {
        const response = await fetch("http://127.0.0.1:5000/post-details/");
        const data = await response.json();

        const allPostsData = [];
        for (let i = 0; i < data.length; i++) {
            if ("title" in data[i] && "firstName" in data[i] && "lastName" in data[i] && "date" in data[i]) {
                allPostsData.push(data[i]);
            }
        }
        console.log(allPostsData);
        setAllPosts(allPostsData);
        console.log(allPosts);
    }

    useEffect(() => {
        fetchPosts();
    }, []);

    useEffect(() => {
        console.log("All Posts: " + allPosts);
    }, [allPosts]);

    return (
        <div>
            <h1>Home Page</h1>
            <p>Welcome to the home page of the Vite React App.</p>
            
            <div>
                {allPosts.map((post, index) => (
                    <PostCard key={index} post={post} />
                ))}
            </div>
        </div>
    );
}