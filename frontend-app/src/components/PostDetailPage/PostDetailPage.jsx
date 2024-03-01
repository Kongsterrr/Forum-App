import React from "react";
import { useParams } from "react-router-dom";
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

  useEffect(async () => {
    console.log(postId);
    const response = await fetch(`http://127.0.0.1:5000/post-details/${postId}`);
    console.log("aaa");
    console.log(response);
    // console.log(response.json());
    const data = await response.json();
    setPostItem(data);
    console.log(data);
  }, []);


    return (
        <div>
            <h1>Post Detail Page</h1>
            <h2>{postItem.title}</h2>
            <p>{postItem.firstName} {postItem.lastName}</p>
            <p>{postItem.dateCreated}</p>
            <p>{postItem.content}</p>
        </div>
    );
}
