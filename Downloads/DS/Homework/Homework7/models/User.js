const mongoose = require('mongoose');

/**
 * User Schema Definition
 * 
 * This schema defines the structure for user documents in MongoDB.
 * Mongoose schemas provide structure and validation for MongoDB collections.
 */
const userSchema = new mongoose.Schema({
    // Username field
    username: {
        type: String,
        required: [true, 'Username is required'], // Field is mandatory
        unique: true, // Ensures no duplicate usernames
        trim: true, // Removes whitespace from beginning and end
        minlength: [3, 'Username must be at least 3 characters'],
        maxlength: [30, 'Username cannot exceed 30 characters']
    },
    
    // Password field (will be hashed before saving)
    password: {
        type: String,
        required: [true, 'Password is required'],
        minlength: [6, 'Password must be at least 6 characters']
        // Note: We don't store plain passwords, only bcrypt hashes
    },
    
    // Role-based access control (RBAC)
    role: {
        type: String,
        enum: ['user', 'admin'], // Only these two roles are allowed
        default: 'user' // Default role if not specified
    }
}, {
    // Schema options
    timestamps: true // Automatically adds createdAt and updatedAt fields
});

/**
 * Export the User Model
 * 
 * mongoose.model() creates a model from the schema.
 * The model name 'User' will create a collection named 'users' in MongoDB
 * (Mongoose automatically pluralizes and lowercases the model name).
 */
module.exports = mongoose.model('User', userSchema);
