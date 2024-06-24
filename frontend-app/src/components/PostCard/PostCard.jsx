import React from "react";
import { Link } from "react-router-dom";
import "./PostCard.css";

export default function PostCard({ post, children }) {
    const handleClick = () => {
        console.log("Clicked");
    }

    const displayDate = post.dateViewed || post.date || post.dateCreated;

    return (
        <div className="card-container">
            <h2>{post.title}</h2>
            <p>{post.firstName} {post.lastName}</p>
            <p>{displayDate}</p>
            {children}
        </div>
            
    );
}