import React from "react";

export default function UserCard({ user }) {
    return (
        <div>
            <h2>{user.title}</h2>
            <p>{user.first_name} {user.last_name}</p>
            <p>{user.date}</p>
        </div>
    );
}