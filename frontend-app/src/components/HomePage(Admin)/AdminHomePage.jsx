import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchPosts, banPost, unbanPost, recoverPost } from '../../store/actions/AdminHomeActions';


export default function AdminHomePage() {
  const dispatch = useDispatch();
  const {postsData} = useSelector(state => state.adminHome);

  useEffect(() => {
    dispatch(fetchPosts()); // Fetch posts when component mounts
  }, [dispatch]);

  // Handlers for ban, unban, and recover actions
  const handleBan = (postId) => {
    dispatch(banPost(postId));
  };

  const handleUnban = (postId) => {
    dispatch(unbanPost(postId));
  };

  const handleRecover = (postId) => {
    dispatch(recoverPost(postId));
  };


  return (
      <div>
        <h1>Admin Home Page</h1>
        <div className="posts-container">
          <section className="posts-section">
            <h2>Published Posts</h2>
            <ul>
              {postsData.published_posts.map((post) => (
                  <li key={post.postId}>
                    <h3>{post.title}</h3>
                    <p>By: {post.firstName} {post.lastName}</p>
                    <p>Date: {post.date}</p>
                    <button onClick={() => handleBan(post.postId)}>Ban</button>
                  </li>
              ))}
            </ul>
          </section>

          <section className="posts-section">
            <h2>Banned Posts</h2>
            <ul>
              {postsData.banned_posts.map((post) => (
                  <li key={post.postId}>
                    <h3>{post.title}</h3>
                    <p>By: {post.firstName} {post.lastName}</p>
                    <p>Date: {post.date}</p>
                    <button onClick={() => handleUnban(post.postId)}>Unban</button>
                  </li>
              ))}
            </ul>
          </section>

          <section className="posts-section">
            <h2>Deleted Posts</h2>
            <ul>
              {postsData.deleted_posts.map((post) => (
                  <li key={post.postId}>
                    <h3>{post.title}</h3>
                    <p>By: {post.firstName} {post.lastName}</p>
                    <p>Date: {post.date}</p>
                    <button onClick={() => handleRecover(post.postId)}>Recover</button>
                  </li>
              ))}
            </ul>
          </section>
        </div>
      </div>
  );
}


// import React, { useEffect, useState } from 'react';
//
// export default function AdminHomePage() {
//   const [postsData, setPostsData] = useState({
//     published_posts: [],
//     banned_posts: [],
//     deleted_posts: []
//   });
//
//   // for testing purpose
//   localStorage.setItem('token', 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5LCJ1c2VyX3N0YXR1cyI6IkFkbWluIiwiZXhwIjoxNzEwMDExOTAzfQ.qk3KkZHajW1ip915L7ExHyVj7wLbq8D-X1QdesruUxk');
//
//   const token = localStorage.getItem('token');
//
//   const fetchPostsData = async () => {
//     try {
//       const response = await fetch('http://127.0.0.1:5000/post-details/admin', {
//         headers: {
//           'Authorization': `${token}`
//         }
//       });
//       const data = await response.json();
//       setPostsData(data);
//     } catch (error) {
//       console.error('Failed to fetch posts data:', error);
//     }
//   };
//
//   useEffect(() => {
//     fetchPostsData();
//   }, []);
//
//
//
//   const handleBan = async (postId) => {
//     try {
//       await fetch(`http://127.0.0.1:5000/post_and_reply/${postId}/banned`, {
//         method: 'PUT',
//         headers: { 'Authorization': `${token}` }
//       });
//       fetchPostsData();
//     } catch (error) {
//       console.error('Failed to ban post:', error);
//     }
//   };
//
//   const handleUnban = async (postId) => {
//     try {
//       await fetch(`http://127.0.0.1:5000/post_and_reply/${postId}/unbanned`, {
//         method: 'PUT',
//         headers: { 'Authorization': `${token}` }
//       });
//       fetchPostsData();
//     } catch (error) {
//       console.error('Failed to unban post:', error);
//     }
//   };
//
//   const handleRecover = async (postId) => {
//     try {
//       await fetch(`http://127.0.0.1:5000/post_and_reply/${postId}/recoverDeleted`, {
//         method: 'PUT',
//         headers: { 'Authorization': `${token}` }
//       });
//       fetchPostsData();
//     } catch (error) {
//       console.error('Failed to recover post:', error);
//     }
//   };
//
//   return (
//     <div>
//       <h1>Admin Home Page</h1>
//       <div className="posts-container">
//         <section className="posts-section">
//           <h2>Published Posts</h2>
//           <ul>
//             {postsData.published_posts.map((post) => (
//               <li key={post.postId}>
//                 <h3>{post.title}</h3>
//                 <p>By: {post.firstName} {post.lastName}</p>
//                 <p>Date: {post.date}</p>
//                 <button onClick={() => handleBan(post.postId)}>Ban</button>
//               </li>
//             ))}
//           </ul>
//         </section>
//
//         <section className="posts-section">
//           <h2>Banned Posts</h2>
//           <ul>
//             {postsData.banned_posts.map((post) => (
//               <li key={post.postId}>
//                 <h3>{post.title}</h3>
//                 <p>By: {post.firstName} {post.lastName}</p>
//                 <p>Date: {post.date}</p>
//                 <button onClick={() => handleUnban(post.postId)}>Unban</button>
//               </li>
//             ))}
//           </ul>
//         </section>
//
//         <section className="posts-section">
//           <h2>Deleted Posts</h2>
//           <ul>
//             {postsData.deleted_posts.map((post) => (
//               <li key={post.postId}>
//                 <h3>{post.title}</h3>
//                 <p>By: {post.firstName} {post.lastName}</p>
//                 <p>Date: {post.date}</p>
//                 <button onClick={() => handleRecover(post.postId)}>Recover</button>
//               </li>
//             ))}
//           </ul>
//         </section>
//       </div>
//     </div>
//   );
//
// }
