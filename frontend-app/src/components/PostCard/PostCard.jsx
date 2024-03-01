import React from "react";
import { Link } from "react-router-dom";
import "./PostCard.css";

export default function PostCard({ post }) {
    const handleClick = () => {
        console.log("Clicked");
    }

    return (
        <Link to={`/post/${post.id}`} className="card-container">
            <h2>{post.title}</h2>
            <p>{post.firstName} {post.lastName}</p>
            <p>{post.date}</p>
        </Link>
    );
}