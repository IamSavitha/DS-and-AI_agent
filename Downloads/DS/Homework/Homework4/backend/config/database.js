/**
 * ============================================
 * DATABASE CONFIGURATION
 * ============================================
 * 
 * CONCEPTS:
 * 1. Sequelize - ORM for Node.js
 * 2. Environment Variables - Secure configuration
 * 3. Connection Pooling - Efficient database connections
 */

const { Sequelize } = require('sequelize');

/**
 * CONCEPT: Sequelize Instance
 * - Creates connection to MySQL database
 * - Uses environment variables for configuration
 * - Supports connection pooling for performance
 */
const sequelize = new Sequelize(
  process.env.DB_NAME || 'book_db',           // Database name
  process.env.DB_USER || 'root',               // Database user
  process.env.DB_PASSWORD || '',               // Database password
  {
    host: process.env.DB_HOST || 'localhost',  // Database host
    port: process.env.DB_PORT || 3306,          // Database port
    dialect: 'mysql',                          // Database type
    logging: process.env.NODE_ENV === 'development' ? console.log : false,
    
    /**
     * CONCEPT: Connection Pool
     * - Manages multiple database connections
     * - max: Maximum connections in pool
     * - min: Minimum connections to maintain
     * - acquire: Time to wait for connection
     * - idle: Time before closing idle connection
     */
    pool: {
      max: 5,        // Maximum 5 connections
      min: 0,        // Minimum 0 connections
      acquire: 30000, // Wait 30 seconds for connection
      idle: 10000    // Close idle connection after 10 seconds
    }
  }
);

module.exports = sequelize;
