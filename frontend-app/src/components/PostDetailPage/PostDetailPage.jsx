import React from "react";
import { Link, useParams } from "react-router-dom";
import { useState, useEffect } from "react";

export default function PostDetailPage({  }) {

  let {postId} = useParams();
  let [postItem, setPostItem] = useState([{
        title: "",
        first_name: "",
        last_name: "",
        dateCreated: "",
        content: "",
    }])

  const fetchPost = async () => {
    try {
        const response = await fetch(`http://127.0.0.1:5000/post-details/${postId}`);
        if (!response.ok) {
            throw new Error("Failed to fetch post details");
        }
        const data = await response.json();
        setPostItem(data);
    } catch (error) {
        console.error("Error fetching post:", error);
    }
};

  useEffect(() => {
    fetchPost();
  }, []);

    return (
        <div>
            <Link to={`/home`}>Back to Home</Link>
            <h1>Post Detail Page</h1>
            <h2>{postItem.title}</h2>
            <p>{postItem.firstName} {postItem.lastName}</p>
            <p>{postItem.dateCreated}</p>
            <p>{postItem.content}</p>
        </div>
    );
}
