/**
 * ============================================
 * BOOK MODEL (Sequelize)
 * ============================================
 * 
 * CONCEPTS:
 * 1. Sequelize Model - Database table representation
 * 2. Data Types - Column type definitions
 * 3. Validation - Data integrity rules
 * 4. Model Definition - Schema structure
 */

const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

/**
 * CONCEPT: Sequelize Model Definition
 * - Defines structure of 'books' table
 * - Each field represents a database column
 * - DataTypes specify column types
 */
const Book = sequelize.define('Book', {
  /**
   * CONCEPT: Primary Key
   * - id is the unique identifier
   * - autoIncrement: true generates sequential IDs
   * - primaryKey: true marks as primary key
   */
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
    allowNull: false
  },
  
  /**
   * CONCEPT: String Type with Validation
   * - STRING(255) stores text up to 255 characters
   * - allowNull: false makes field required
   * - validate: {} adds custom validation rules
   */
  title: {
    type: DataTypes.STRING(255),
    allowNull: false,
    validate: {
      notEmpty: {
        msg: 'Book title cannot be empty'
      },
      len: {
        args: [1, 255],
        msg: 'Title must be between 1 and 255 characters'
      }
    }
  },
  
  /**
   * CONCEPT: String Type
   * - Stores author name
   * - Required field with validation
   */
  author: {
    type: DataTypes.STRING(255),
    allowNull: false,
    validate: {
      notEmpty: {
        msg: 'Author name cannot be empty'
      },
      len: {
        args: [1, 255],
        msg: 'Author name must be between 1 and 255 characters'
      }
    }
  },
  
  /**
   * CONCEPT: Timestamps
   * - createdAt: Automatically set when record is created
   * - updatedAt: Automatically updated when record changes
   * - Managed by Sequelize automatically
   */
}, {
  tableName: 'books',  // Explicit table name
  timestamps: true,    // Enable createdAt and updatedAt
  underscored: false    // Use camelCase for column names
});

module.exports = Book;
