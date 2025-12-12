"""
train_customer_model.py
========================
This script trains a K-Means clustering model for customer segmentation.

CONCEPTS COVERED:
1. Data Simulation: Creating synthetic datasets for machine learning
2. K-Means Clustering: Unsupervised learning algorithm for grouping data
3. Model Serialization: Saving trained models using pickle
4. Metadata Management: Storing additional information alongside models
"""

import numpy as np
from sklearn.cluster import KMeans
import pickle
import os

# ============================================================================
# CONCEPT 1: DATA SIMULATION
# ============================================================================
# Data simulation is the process of generating synthetic data that mimics
# real-world patterns. This is useful when:
# - Real data is unavailable or sensitive
# - Testing algorithms before production deployment
# - Creating reproducible datasets for demonstrations
#
# We use numpy's random number generation to create realistic customer data
# with controlled distributions for Annual Income and Spending Score.

def simulate_customer_data(n_samples=200, random_state=42):
    """
    Simulates customer data with Annual Income and Spending Score.
    
    Parameters:
    -----------
    n_samples : int
        Number of customers to simulate (default: 200)
    random_state : int
        Random seed for reproducibility (default: 42)
    
    Returns:
    --------
    data : numpy.ndarray
        2D array of shape (n_samples, 2) containing [Annual Income, Spending Score]
    """
    # Set random seed for reproducibility
    # CONCEPT: Reproducibility is crucial in ML - same seed = same results
    np.random.seed(random_state)
    
    # Simulate Annual Income (in thousands of dollars)
    # Using normal distribution: mean=60k, std=15k, clipped to reasonable range
    # CONCEPT: Normal distribution models many real-world phenomena
    annual_income = np.random.normal(loc=60, scale=15, size=n_samples)
    annual_income = np.clip(annual_income, 15, 140)  # Clamp to realistic range
    
    # Simulate Spending Score (1-100 scale)
    # Using uniform distribution for variety
    # CONCEPT: Uniform distribution ensures equal probability across range
    spending_score = np.random.uniform(low=1, high=100, size=n_samples)
    
    # Combine into 2D array: each row is one customer
    # CONCEPT: NumPy arrays are efficient for numerical computations
    data = np.column_stack([annual_income, spending_score])
    
    return data


# ============================================================================
# CONCEPT 2: K-MEANS CLUSTERING
# ============================================================================
# K-Means is an unsupervised learning algorithm that partitions data into
# k clusters by:
# 1. Initializing k centroids (cluster centers) randomly
# 2. Assigning each point to the nearest centroid
# 3. Updating centroids to the mean of assigned points
# 4. Repeating steps 2-3 until convergence
#
# Key properties:
# - Requires specifying k (number of clusters) beforehand
# - Works well with spherical, well-separated clusters
# - Sensitive to initialization (k-means++ helps)
# - Used for customer segmentation, image compression, etc.

def train_kmeans_model(data, n_clusters=5, random_state=42):
    """
    Trains a K-Means clustering model on customer data.
    
    Parameters:
    -----------
    data : numpy.ndarray
        Customer data with shape (n_samples, 2)
    n_clusters : int
        Number of clusters (default: 5)
    random_state : int
        Random seed for model initialization (default: 42)
    
    Returns:
    --------
    model : sklearn.cluster.KMeans
        Trained K-Means model
    """
    # Initialize KMeans model
    # CONCEPT: n_clusters=k determines how many customer segments we want
    #          init='k-means++' uses smart initialization (better than random)
    #          n_init=10 runs the algorithm 10 times and picks the best result
    #          random_state ensures reproducible results
    model = KMeans(
        n_clusters=n_clusters,
        init='k-means++',  # Smart centroid initialization
        n_init=10,         # Number of times to run with different initializations
        max_iter=300,      # Maximum iterations per run
        random_state=random_state
    )
    
    # Train the model (fit to data)
    # CONCEPT: 'fit' is the training step - model learns cluster centers
    model.fit(data)
    
    print(f"✓ Model trained successfully with {n_clusters} clusters")
    print(f"✓ Cluster centers:\n{model.cluster_centers_}")
    
    return model


# ============================================================================
# CONCEPT 3: MODEL SERIALIZATION (PICKLING)
# ============================================================================
# Serialization converts Python objects into byte streams for storage/transmission.
# Pickle is Python's native serialization format.
#
# Why serialize models?
# - Save trained models to disk (avoid retraining)
# - Deploy models to production
# - Share models between systems
# - Version control model artifacts
#
# Security Note: Only unpickle data from trusted sources!

def save_model_and_metadata(model, data, model_filename, metadata_filename):
    """
    Saves the trained model and metadata to pickle files.
    
    Parameters:
    -----------
    model : sklearn.cluster.KMeans
        Trained K-Means model
    data : numpy.ndarray
        Original training data
    model_filename : str
        Path to save the model
    metadata_filename : str
        Path to save the metadata
    """
    # Save the trained model
    # CONCEPT: 'wb' = write binary mode (required for pickle)
    with open(model_filename, 'wb') as f:
        pickle.dump(model, f)
    print(f"✓ Model saved to {model_filename}")
    
    # Prepare metadata dictionary
    # CONCEPT: Metadata stores additional information needed for inference
    #          Feature names: what each column represents
    #          Cluster centers: for visualization and analysis
    metadata = {
        'feature_names': ['Annual Income (k$)', 'Spending Score (1-100)'],
        'cluster_centers': model.cluster_centers_,
        'n_clusters': model.n_clusters,
        'training_data': data  # Optional: for visualization in app
    }
    
    # Save metadata
    with open(metadata_filename, 'wb') as f:
        pickle.dump(metadata, f)
    print(f"✓ Metadata saved to {metadata_filename}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("CUSTOMER SEGMENTATION MODEL TRAINING")
    print("=" * 60)
    
    # Step 1: Simulate customer data
    print("\n[Step 1] Simulating customer data...")
    customer_data = simulate_customer_data(n_samples=200, random_state=42)
    print(f"✓ Generated {len(customer_data)} customer records")
    print(f"  - Annual Income range: ${customer_data[:, 0].min():.1f}k - ${customer_data[:, 0].max():.1f}k")
    print(f"  - Spending Score range: {customer_data[:, 1].min():.1f} - {customer_data[:, 1].max():.1f}")
    
    # Step 2: Train K-Means model
    print("\n[Step 2] Training K-Means model (k=5)...")
    kmeans_model = train_kmeans_model(customer_data, n_clusters=5, random_state=42)
    
    # Step 3: Save model and metadata
    print("\n[Step 3] Saving model and metadata...")
    # Note: Replace 'yourname' with your actual name
    model_file = 'customer_kmeans_model_yourname.pkl'
    metadata_file = 'customer_metadata.pkl'
    
    save_model_and_metadata(
        kmeans_model,
        customer_data,
        model_file,
        metadata_file
    )
    
    print("\n" + "=" * 60)
    print("TRAINING COMPLETE!")
    print("=" * 60)
    print(f"\nNext steps:")
    print(f"1. Run: streamlit run customer_segmentation_app.py")
    print(f"2. The app will load {model_file} and {metadata_file}")
