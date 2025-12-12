# Quick Start Guide - HW6

## 🚀 Getting Started in 5 Minutes

### Step 1: Backend Setup (2 minutes)

```bash
# Navigate to project directory
cd Homework6

# Install dependencies
npm install

# Create .env file (copy from env.template)
cp env.template .env

# Edit .env and add your MongoDB connection string
# For local: mongodb://localhost:27017/productdb
# For Atlas: mongodb+srv://YOUR_USERNAME:YOUR_PASSWORD@YOUR_CLUSTER.mongodb.net/productdb

# Start MongoDB (if local)
# macOS: brew services start mongodb-community
# Linux: sudo systemctl start mongod

# Start server
npm start
```

✅ Backend running on http://localhost:5000

### Step 2: Frontend Setup (3 minutes)

```bash
# In a new terminal, create React app (if needed)
npx create-react-app product-frontend
cd product-frontend

# Install axios
npm install axios

# Copy App.js and App.css from Homework6 directory
# Replace src/App.js and src/App.css

# Start React app
npm start
```

✅ Frontend running on http://localhost:3000

### Step 3: Test the Application

1. Open http://localhost:3000 in your browser
2. Fill out the form to create a product
3. Click "Add Product"
4. See your product appear in the list below
5. Try editing and deleting products

## 📋 Checklist

- [ ] MongoDB is running (local or Atlas)
- [ ] Backend server is running (port 5000)
- [ ] Frontend React app is running (port 3000)
- [ ] .env file is configured with MongoDB URI
- [ ] Can see "Product Management API is running" at http://localhost:5000

## 🐛 Common Issues

**"MongoDB connection error"**
- Check if MongoDB is running
- Verify MONGODB_URI in .env file
- For Atlas: Check network access settings

**"Cannot GET /"**
- Make sure backend server is running
- Check port 5000 is not in use

**"Network Error" in React**
- Ensure backend is running
- Check CORS is enabled in server.js
- Verify API_URL in App.js matches backend port

**"Module not found"**
- Run `npm install` in backend directory
- Run `npm install axios` in frontend directory

## 📚 Next Steps

- Read `HW6_CONCEPTS_EXPLANATION.md` for detailed explanations
- Review `README.md` for full documentation
- Explore the code and understand each concept

## 🎓 Learning Objectives

After completing this homework, you should understand:

1. ✅ How to create a RESTful API with Express
2. ✅ How to use MongoDB with Mongoose
3. ✅ How to build a React frontend
4. ✅ How frontend and backend communicate
5. ✅ How to handle async operations
6. ✅ How to manage state in React
7. ✅ How to handle errors gracefully

Happy coding! 🎉
