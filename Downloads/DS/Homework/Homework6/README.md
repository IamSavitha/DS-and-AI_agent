# Homework 6: Product Management System

A full-stack MERN (MongoDB, Express, React, Node.js) application for managing products.

## Features

- ✅ Create new products
- ✅ View all products
- ✅ Update existing products
- ✅ Delete products
- ✅ Form validation
- ✅ Error handling
- ✅ Responsive design

## Project Structure

```
Homework6/
├── server.js              # Express server entry point
├── Product.js             # Mongoose schema/model
├── routes/
│   └── products.js        # API routes for products
├── App.js                 # React frontend component
├── App.css                # Styling
├── package.json           # Backend dependencies
├── package-frontend.json  # Frontend dependencies (rename to package.json in React app)
└── README.md              # This file
```

## Prerequisites

- Node.js (v14 or higher)
- MongoDB (local installation or MongoDB Atlas account)
- npm or yarn

## Installation

### Backend Setup

1. Install backend dependencies:
```bash
npm install
```

2. Create a `.env` file in the root directory:
```env
MONGODB_URI=mongodb://localhost:27017/productdb
PORT=5000
```

For MongoDB Atlas, use:
```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/productdb
PORT=5000
```

3. Start MongoDB (if using local installation):
```bash
# macOS with Homebrew
brew services start mongodb-community

# Linux
sudo systemctl start mongod

# Windows
net start MongoDB
```

4. Start the backend server:
```bash
npm start
# or for development with auto-reload
npm run dev
```

The server will run on `http://localhost:5000`

### Frontend Setup

1. If you don't have a React app, create one:
```bash
npx create-react-app product-management-frontend
cd product-management-frontend
```

2. Install axios:
```bash
npm install axios
```

3. Replace the default `src/App.js` with the provided `App.js`

4. Replace the default `src/App.css` with the provided `App.css`

5. Start the React development server:
```bash
npm start
```

The frontend will run on `http://localhost:3000`

## API Endpoints

### Base URL: `http://localhost:5000/api/products`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products` | Get all products |
| GET | `/api/products/:id` | Get a single product by ID |
| POST | `/api/products` | Create a new product |
| PUT | `/api/products/:id` | Update a product |
| DELETE | `/api/products/:id` | Delete a product |

### Example API Request

**Create a product:**
```bash
curl -X POST http://localhost:5000/api/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop",
    "description": "High-performance laptop",
    "price": 999.99,
    "quantity": 10,
    "category": "Electronics"
  }'
```

## Product Schema

```javascript
{
  name: String (required, max 100 chars),
  description: String (optional),
  price: Number (required, min 0),
  quantity: Number (default 0, min 0),
  category: String (enum: ['Electronics', 'Clothing', 'Food', 'Books', 'Other'], default 'Other'),
  createdAt: Date (auto-generated),
  updatedAt: Date (auto-generated)
}
```

## Technologies Used

### Backend
- **Node.js** - JavaScript runtime
- **Express.js** - Web framework
- **MongoDB** - NoSQL database
- **Mongoose** - MongoDB object modeling
- **CORS** - Cross-origin resource sharing
- **dotenv** - Environment variable management

### Frontend
- **React** - UI library
- **Axios** - HTTP client
- **CSS3** - Styling

## Concepts Covered

1. **RESTful API Design** - Standard HTTP methods and status codes
2. **MongoDB & NoSQL** - Document-based database
3. **Mongoose ODM** - Schema definition and validation
4. **React Hooks** - useState and useEffect
5. **Async/Await** - Asynchronous programming
6. **CORS** - Cross-origin resource sharing
7. **Environment Variables** - Configuration management
8. **Error Handling** - Try-catch and user feedback

## Troubleshooting

### MongoDB Connection Error
- Ensure MongoDB is running
- Check MONGODB_URI in `.env` file
- Verify network connectivity for MongoDB Atlas

### CORS Errors
- Ensure backend CORS middleware is enabled
- Check that frontend URL matches CORS configuration

### Port Already in Use
- Change PORT in `.env` file
- Or kill the process using the port:
  ```bash
  # Find process
  lsof -i :5000
  # Kill process
  kill -9 <PID>
  ```

## Development Tips

1. Use `nodemon` for auto-restart during development
2. Check browser console for frontend errors
3. Check terminal for backend errors
4. Use Postman or curl to test API endpoints
5. Check MongoDB Compass to view database contents

## Next Steps

- Add user authentication
- Implement search and filtering
- Add pagination
- Implement image uploads
- Add product reviews
- Deploy to cloud (Heroku, AWS, etc.)

## License

This project is for educational purposes.
