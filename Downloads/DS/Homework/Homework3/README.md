# Homework 3: Session-Based Authentication

## Overview

This project implements session-based authentication using Express.js, demonstrating how to manage user sessions, hash passwords, and protect routes.

## Features

- ✅ User login with password authentication
- ✅ Session management using express-session
- ✅ Password hashing with bcrypt
- ✅ Protected routes (dashboard)
- ✅ EJS templating for views
- ✅ Secure logout functionality

## Project Structure

```
Homework3/
├── app.js                 # Main Express application
├── routes/
│   └── auth.js            # Authentication routes
├── middleware/
│   └── auth.js            # Authentication middleware
├── views/
│   ├── index.ejs          # Home page
│   ├── login.ejs          # Login page
│   └── dashboard.ejs      # Protected dashboard
├── package.json           # Dependencies
└── README.md              # This file
```

## Installation

1. Install dependencies:
```bash
npm install
```

## Running the Application

1. Start the server:
```bash
npm start
```

2. Open your browser and navigate to:
```
http://localhost:3000
```

## Demo Credentials

- **Username:** `admin`
- **Password:** `password`

- **Username:** `user`
- **Password:** `user123`

## Key Concepts Covered

1. **Session Management**: Server-side session storage
2. **Password Hashing**: Using bcrypt for secure password storage
3. **Route Protection**: Middleware for authenticated routes
4. **EJS Templating**: Server-side rendering
5. **Express Middleware**: Request processing pipeline

## Documentation

See `HW3_CONCEPTS_EXPLANATION.md` for detailed explanations of all concepts and line-by-line code analysis.

## Technologies Used

- **Express.js**: Web framework
- **express-session**: Session management
- **bcryptjs**: Password hashing
- **EJS**: Templating engine
- **Bootstrap**: UI styling
