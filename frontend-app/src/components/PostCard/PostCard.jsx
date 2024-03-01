import React from "react";

export default function PostCard({ post }) {
    return (
        <div>
            <h2>{post.title}</h2>
            <p>{post.firstName} {post.lastName}</p>
            <p>{post.date}</p>
        </div>
    );
}