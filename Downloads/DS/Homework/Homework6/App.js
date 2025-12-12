import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = 'http://localhost:5000/api/products';

function App() {
  const [products, setProducts] = useState([]);
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    price: '',
    quantity: '',
    category: 'Other'
  });
  const [editingId, setEditingId] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      const response = await axios.get(API_URL);
      setProducts(response.data);
      setError('');
    } catch (err) {
      setError('Failed to fetch products');
    }
  };

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingId) {
        await axios.put(`${API_URL}/${editingId}`, formData);
        setEditingId(null);
      } else {
        await axios.post(API_URL, formData);
      }
      setFormData({ name: '', description: '', price: '', quantity: '', category: 'Other' });
      fetchProducts();
      setError('');
    } catch (err) {
      setError(err.response?.data?.message || 'Operation failed');
    }
  };

  const handleEdit = (product) => {
    setFormData({
      name: product.name,
      description: product.description,
      price: product.price,
      quantity: product.quantity,
      category: product.category
    });
    setEditingId(product._id);
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this product?')) {
      try {
        await axios.delete(`${API_URL}/${id}`);
        fetchProducts();
        setError('');
      } catch (err) {
        setError('Failed to delete product');
      }
    }
  };

  const handleCancel = () => {
    setFormData({ name: '', description: '', price: '', quantity: '', category: 'Other' });
    setEditingId(null);
  };

  return (
    <div className="App">
      <div className="container">
        <h1>Product Management System</h1>
        
        {error && <div className="error">{error}</div>}

        <div className="form-container">
          <h2>{editingId ? 'Edit Product' : 'Add New Product'}</h2>
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              name="name"
              placeholder="Product Name"
              value={formData.name}
              onChange={handleInputChange}
              required
            />
            <textarea
              name="description"
              placeholder="Description"
              value={formData.description}
              onChange={handleInputChange}
              rows="3"
            />
            <input
              type="number"
              name="price"
              placeholder="Price"
              value={formData.price}
              onChange={handleInputChange}
              step="0.01"
              min="0"
              required
            />
            <input
              type="number"
              name="quantity"
              placeholder="Quantity"
              value={formData.quantity}
              onChange={handleInputChange}
              min="0"
              required
            />
            <select
              name="category"
              value={formData.category}
              onChange={handleInputChange}
            >
              <option value="Electronics">Electronics</option>
              <option value="Clothing">Clothing</option>
              <option value="Food">Food</option>
              <option value="Books">Books</option>
              <option value="Other">Other</option>
            </select>
            <div className="button-group">
              <button type="submit" className="btn-primary">
                {editingId ? 'Update' : 'Add'} Product
              </button>
              {editingId && (
                <button type="button" onClick={handleCancel} className="btn-secondary">
                  Cancel
                </button>
              )}
            </div>
          </form>
        </div>

        <div className="products-container">
          <h2>Products List</h2>
          {products.length === 0 ? (
            <p className="no-products">No products available. Add your first product!</p>
          ) : (
            <div className="products-grid">
              {products.map((product) => (
                <div key={product._id} className="product-card">
                  <div className="product-header">
                    <h3>{product.name}</h3>
                    <span className="category-badge">{product.category}</span>
                  </div>
                  <p className="description">{product.description || 'No description'}</p>
                  <div className="product-details">
                    <p><strong>Price:</strong> ${product.price.toFixed(2)}</p>
                    <p><strong>Quantity:</strong> {product.quantity}</p>
                  </div>
                  <div className="product-actions">
                    <button onClick={() => handleEdit(product)} className="btn-edit">
                      Edit
                    </button>
                    <button onClick={() => handleDelete(product._id)} className="btn-delete">
                      Delete
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;