import React from "react";
import { Link, useParams } from "react-router-dom";
import { useState, useEffect } from "react";

export default function PostDetailPage({  }) {

  let {postId} = useParams();
  const [postItem, setPostItem] = useState({
    title: "",
    content: "",
    dateCreated: "",
    dateModified: "",
    replies: [],
    user: {
        firstName: "",
        lastName: "",
        profileImage: ""
    }
  });

  const fetchPost = async () => {
    try {
        const response = await fetch(`http://127.0.0.1:5000/post-details/${postId}`);
        if (!response.ok) {
            throw new Error("Failed to fetch post details");
        }
        const data = await response.json();
        setPostItem(data);
        console.log(data);
        console.log(postItem);
    } catch (error) {
        console.error("Error fetching post:", error);
    }
};

  useEffect(() => {
    console.log(localStorage.getItem("token"));
    fetchPost();
    createViewHistory();
  }, []);

  const createViewHistory = async () => {
    try {
        const response = await fetch("http://127.0.0.1:5000/history/", {
            method: "POST",
            headers: {
              "Authorization": `Bearer ${localStorage.getItem("token")}`,
              "Content-Type": "application/json" // Set content type to JSON
            },
            body: JSON.stringify({ "postId": postId }) // Stringify the request body
        });
        if (!response.ok) {
            throw new Error("Failed to create history");
        }
    } catch (error) {
        console.error("Error creating history:", error);
    }
};

    return (
        <div>
            <Link to={`/home`}>Back to Home</Link>
            <h1>Post Detail Page</h1>
            <h2>{postItem.title}</h2>
            <p>Posted By: {postItem.user.firstName} {postItem.user.lastName} on {postItem.dateCreated}</p>
            <p>{postItem.content}</p>
            <ul>
                {postItem.replies.map((reply) => (
                    <li key={reply.id}>
                      <p>{reply.comment}</p>
                      <p>comment by {reply.firstName} {reply.lastName} on {reply.dateCreated} </p>
                    </li>
                ))}
            </ul>
            
        </div>
    );
}
