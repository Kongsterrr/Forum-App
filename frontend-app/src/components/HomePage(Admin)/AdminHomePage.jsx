import React, { useEffect, useState } from 'react';

export default function AdminHomePage() {
  const [postsData, setPostsData] = useState({
    published_posts: [],
    banned_posts: [],
    deleted_posts: []
  });

  // for testing purpose
  localStorage.setItem('token', 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5LCJ1c2VyX3N0YXR1cyI6IkFkbWluIiwiZXhwIjoxNzEwMDExOTAzfQ.qk3KkZHajW1ip915L7ExHyVj7wLbq8D-X1QdesruUxk');

  const fetchPostsData = async () => {
    const token = localStorage.getItem('token');
    try {
      const response = await fetch('http://127.0.0.1:5000/post-details/admin', {
        headers: {
          'Authorization': `${token}`
        }
      });
      const data = await response.json();
      setPostsData(data);
    } catch (error) {
      console.error('Failed to fetch posts data:', error);
    }
  };

  useEffect(() => {
    fetchPostsData();
  }, []);

  return (
    <div>
      <h1>Admin Home Page</h1>
      <section>
        <h2>Published Posts</h2>
        <ul>
          {postsData.published_posts.map((post, index) => (
            <li key={post.postId}>
              <h3>{post.title}</h3>
              <p>By: {post.firstName} {post.lastName}</p>
              <p>Date: {post.date}</p>
            </li>
          ))}
        </ul>
      </section>


      <section>
        <h2>Banned Posts</h2>
        <ul>
          {postsData.banned_posts.map((post, index) => (
            <li key={post.postId}>
              <h3>{post.title}</h3>
              <p>By: {post.firstName} {post.lastName}</p>
              <p>Date: {post.date}</p>
            </li>
          ))}
        </ul>
      </section>


      <section>
        <h2>Deleted Posts</h2>
        <ul>
          {postsData.deleted_posts.map((post, index) => (
            <li key={post.postId}>
              <h3>{post.title}</h3>
              <p>By: {post.firstName} {post.lastName}</p>
              <p>Date: {post.date}</p>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
