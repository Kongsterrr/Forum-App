# FA-Forum Project

## Description
FA-Forum is a comprehensive forum application built using a Microservices architecture. It features distinct user roles with different permissions, a robust backend using Flask, and frontend developed in React. The project leverages several AWS services for efficient operation, including RDS for database management and S3 Buckets for file storage.

## Features
### General
Services Diagram: https://drive.google.com/file/d/1F0TJUsSgpBRfgQxqt7P9CZrsrrrTHWkZ/view?usp=sharing
Microservices Architecture: Independent services for user management, posts, messaging, and files.
JWT Authentication: Ensures secure access to the application endpoints.
React Frontend: A dynamic and responsive UI with global navigation accessible on all pages.
Flask Backend: Utilizing Flask-rest and SQLAlchemy over a MySQL database hosted on AWS RDS.

### User Roles and Permissions
Visitor/Banned User: Limited access to basic pages like login and register.
Normal User: Can view and reply to published posts, create posts after email verification.
Post Owner: Additional rights to modify or delete their posts and control visibility.
Admin and Super Admin Roles: Manage users, posts, and site-wide settings with advanced permissions.

### Pages
Login and Registration: Secure user authentication with email verification.
User and Admin Dashboards: Custom interfaces for regular users and administrators.
Post Interaction: Detailed post pages with reply functionalities and the ability to manage post status.

## Setup
### Prerequisites
Python 3.x
MySQL
AWS Account

### Installation
1. Clone the Repository:
   https://github.com/BF-2024-Jan-Python/Forum-App---Blue-Team.git
   cd Forum-App---Blue-Team
2. Set up the Backend
   a. Navigate to each service's directory:
      cd <service-name> (e.g. cd Forum-AuthService)
   b. Install the necessary dependencies:
      pip install -r requirements.txt
   c. Start the service using Flask:
      python -m flask run
4. Set up the Frontend
   cd frontend-app
   npm install
   npm run dev

## Usage
Visit http://localhost:3000 to access the frontend.
Use the provided Postman collection for backend API testing.

## Microservices Architecture
### 1. Gateway Service
Function: Serves as the entry point for all requests to the backend system and routes them to the appropriate microservice.
Technologies: N/A
### 2. Authentication Service
Function: Handles authentication and authorization, ensuring secure access to the application's resources.
Technologies: Flask, JWT
### 3. User Service
Function: Manages all user-related operations like registration, user profile updates, and user data management.
Technologies: Flask, SQLAlchemy, MySQL
### 4. Post and Reply Service
Function: Manages the creation, modification, and viewing of posts and replies.
Technologies: Flask, SQLAlchemy, MySQL
### 5. History Service
Function: Tracks and stores user interaction history with posts.
Technologies: Flask, SQLAlchemy, MySQL
### 6. Message Service
Function: Manages messaging between users and administrators.
Technologies: Flask, SQLAlchemy, MySQL
### 7. File Service
Function: Handles file uploads and storage, such as user profile images and post attachments.
Technologies: Flask, AWS S3
### 8. Email Service
Function: Manages sending emails to users, such as registration confirmation and notifications.
Technologies: RabbitMQ, Flask-Mail
### 9. Post Detail Service (Composite Service)
Function: Aggregates data from the Post and Reply Service and User Service to provide detailed information about posts, including user interactions and post content.
Interactions: Retrieves user profiles from User Service and post details from Post and Reply Service.
Technologies: Flask, SQLAlchemy, MySQL
### 10. Post History Service (Composite Service)
Function: Integrates data from the User Service, Post and Reply Service, and History Service to provide a comprehensive history of user interactions with posts.
Interactions: Combines user data, post content, and historical interactions to create detailed historical views.
Technologies: Flask, SQLAlchemy, MySQL
