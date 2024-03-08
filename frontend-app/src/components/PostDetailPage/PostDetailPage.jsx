import React from "react";
import { Link, useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import AddReplyPage from "./AddReplyPage";


export default function PostDetailPage({  }) {

  let {postId} = useParams();
  const [postItem, setPostItem] = useState({
    title: "",
    content: "",
    status: "",
    dateCreated: "",
    dateModified: "",
    images: {url: ""},
    replies: [],
    user: {
        firstName: "",
        lastName: "",
        profileImage: ""
    }

  });

  const [showAddReply, setShowAddReply] = useState(false);
  const toggleAddReply = () => {
    setShowAddReply(!showAddReply);
  };

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

  const publishPost = async () => {
  try {
    const response = await fetch(`http://127.0.0.1:5000/post_and_reply/${postId}/publish`, {
      method: "PUT",
      headers: {
        "Authorization": `Bearer ${localStorage.getItem("token")}`
      },
    });
    if (!response.ok) {
      throw new Error("Failed to publish post");
    }
   setPostItem(prevState => ({
      ...prevState,
      status: "Published"
    }));
    console.log("Post published successfully");
  } catch (error) {
    console.error("Error publishing post:", error);
  }
};


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
            <h2>{postItem.title}</h2>
            <p>Posted By: {postItem.user.firstName} {postItem.user.lastName} on {postItem.dateCreated}</p>
            <p>Content: {postItem.content}</p>
            <p>Status: {postItem.status}</p>
            <div>
                    {postItem.images != null && postItem.images.url.length > 0? (
                        <div>
                            <p>Images:</p>
                            <img src={postItem.images.url} alt="Post Image" />
                            {/* <ul>
                            {postItem.images.urls.map((url, index) => (
                                <li key={index}>
                                <img src={postItem.images.url} alt={`Image ${index}`} />
                                <div>{url}</div>
                                </li>
                            ))}
                            </ul> */}
                        </div>
                        
                    )
                    : (
                        <p></p>
                    )}
            </div>

            {postItem.status === "Unpublished" && (
            <button onClick={publishPost}>Publish Post</button>
            )}

            
            
            <br></br>
            
            <h2>Replies:</h2>
            <ul>
                {postItem.replies.map((reply) => (
                    <li key={reply.id}>
                      <p>{reply.comment}</p>
                      <p>comment by {reply.firstName} {reply.lastName} on {reply.dateCreated} </p>
                    </li>
                ))}
            </ul>

            <button onClick={toggleAddReply}>Reply to the Post</button>

            <AddReplyPage open={showAddReply} onClose={toggleAddReply} postId={postId} fetchPost={fetchPost} />

            
        </div>
    );
}
