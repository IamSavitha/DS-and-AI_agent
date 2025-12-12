"""
customer_segmentation_app.py
=============================
Streamlit application for customer segmentation using K-Means clustering.

CONCEPTS COVERED:
1. Streamlit Framework: Rapid web app development for ML
2. Caching: Optimizing performance with @st.cache_resource
3. Interactive Widgets: User input via sliders
4. Data Visualization: Matplotlib/Plotly for scatter plots
5. Model Inference: Making predictions with trained models
"""

import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# ============================================================================
# CONCEPT 1: STREAMLIT CACHING (@st.cache_resource)
# ============================================================================
# Caching prevents expensive operations from running on every app rerun.
# 
# @st.cache_resource:
# - Caches objects that shouldn't be copied (models, database connections)
# - Stores in memory, persists across reruns
# - Automatically invalidates if function code changes
#
# Why cache model loading?
# - Model files can be large (MBs to GBs)
# - Loading from disk is slow
# - Model doesn't change during app session
# - Improves user experience (faster app)

@st.cache_resource
def load_resources(model_file, metadata_file):
    """
    Loads the pickled model and metadata with caching.
    
    CONCEPT: This function runs once and results are cached.
             Subsequent calls return cached results instantly.
    
    Parameters:
    -----------
    model_file : str
        Path to the pickled model file
    metadata_file : str
        Path to the pickled metadata file
    
    Returns:
    --------
    model : sklearn.cluster.KMeans or None
        Loaded K-Means model
    metadata : dict or None
        Dictionary containing feature names, cluster centers, etc.
    """
    try:
        # Check if files exist
        if not os.path.exists(model_file) or not os.path.exists(metadata_file):
            st.error("Required model or metadata files not found. Please run 'train_customer_model.py' first!")
            return None, None
        
        # Load model from pickle file
        # CONCEPT: 'rb' = read binary mode (required for pickle)
        with open(model_file, 'rb') as f:
            model = pickle.load(f)
        
        # Load metadata from pickle file
        with open(metadata_file, 'rb') as f:
            metadata = pickle.load(f)
        
        return model, metadata
    
    except Exception as e:
        # Error handling: inform user if loading fails
        st.error(f"Error loading resources: {e}")
        return None, None


# ============================================================================
# CONCEPT 2: STREAMLIT UI COMPONENTS
# ============================================================================
# Streamlit provides simple Python functions to create UI elements:
# - st.title(): Main heading
# - st.sidebar: Sidebar container for inputs
# - st.slider(): Interactive slider for numeric input
# - st.button(): Clickable button
# - st.metric(): Display key metrics
# - st.pyplot(): Display matplotlib plots

# Page configuration (appears in browser tab)
st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="👥",
    layout="wide"
)

# App title and description
st.title('👥 Customer Segmentation Dashboard')
st.markdown('**Predict customer cluster based on Annual Income and Spending Score**')
st.markdown('---')

# Load model and metadata (cached)
MODEL_FILE = 'customer_kmeans_model_yourname.pkl'
METADATA_FILE = 'customer_metadata.pkl'

model, metadata = load_resources(MODEL_FILE, METADATA_FILE)

# ============================================================================
# MAIN APPLICATION LOGIC
# ============================================================================

if model is not None and metadata is not None:
    # Extract metadata
    FEATURE_NAMES = metadata['feature_names']
    CLUSTER_CENTERS = metadata['cluster_centers']
    TRAINING_DATA = metadata.get('training_data', None)
    
    # ========================================================================
    # CONCEPT 3: INTERACTIVE INPUT WIDGETS (SIDEBAR)
    # ========================================================================
    # Sidebar keeps inputs organized and doesn't clutter main content area.
    # Sliders provide intuitive way to input numeric values.
    
    st.sidebar.header('📊 Customer Input Parameters')
    
    # Slider for Annual Income
    # CONCEPT: st.sidebar.slider(label, min, max, default, step)
    #          Returns the current slider value
    annual_income = st.sidebar.slider(
        FEATURE_NAMES[0],      # Label
        15.0,                  # Minimum value (15k)
        140.0,                 # Maximum value (140k)
        60.0,                  # Default value
        1.0                    # Step size (1k increments)
    )
    
    # Slider for Spending Score
    spending_score = st.sidebar.slider(
        FEATURE_NAMES[1],      # Label
        1.0,                   # Minimum value
        100.0,                 # Maximum value
        50.0,                  # Default value
        1.0                    # Step size
    )
    
    st.sidebar.markdown('---')
    st.sidebar.info('💡 Adjust the sliders to see how different customer profiles are segmented.')
    
    # ========================================================================
    # CONCEPT 4: MODEL INFERENCE (PREDICTION)
    # ========================================================================
    # Inference is using a trained model to make predictions on new data.
    # Steps:
    # 1. Prepare input in correct format (2D array for sklearn)
    # 2. Call model.predict() method
    # 3. Get cluster ID (integer 0 to k-1)
    
    # Prepare input features
    # CONCEPT: sklearn expects 2D array: shape (n_samples, n_features)
    #          Even for single prediction, use [[feature1, feature2]]
    input_features = np.array([[annual_income, spending_score]])
    
    # Make prediction when button is clicked
    if st.button('🔮 Predict Customer Cluster', type='primary'):
        
        # Predict cluster ID
        # CONCEPT: model.predict() returns array of cluster IDs
        #          [0] extracts first (and only) prediction
        cluster_id = model.predict(input_features)[0]
        
        # ====================================================================
        # CONCEPT 5: DISPLAYING RESULTS
        # ====================================================================
        
        st.subheader('📈 Prediction Result')
        
        # Display cluster ID using metric widget
        # CONCEPT: st.metric() displays key-value pairs prominently
        st.metric(
            label="**Predicted Cluster ID**",
            value=f"Cluster {cluster_id}",
            delta=f"Out of {model.n_clusters} clusters"
        )
        
        # Display input values for confirmation
        st.subheader('📋 Input Data Used')
        input_df = pd.DataFrame(
            input_features,
            columns=FEATURE_NAMES
        )
        st.dataframe(input_df, use_container_width=True)
        
        # ====================================================================
        # CONCEPT 6: DATA VISUALIZATION (SCATTER PLOT)
        # ====================================================================
        # Visualization helps users understand:
        # - Where their input falls in the data space
        # - Cluster boundaries and centers
        # - Relationship between features
        
        st.subheader('📊 Customer Segmentation Visualization')
        
        # Create matplotlib figure
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot training data points (if available)
        if TRAINING_DATA is not None:
            # Get cluster assignments for all training data
            training_clusters = model.predict(TRAINING_DATA)
            
            # Plot each cluster with different color
            # CONCEPT: Color coding helps distinguish clusters visually
            colors = ['red', 'blue', 'green', 'orange', 'purple']
            for i in range(model.n_clusters):
                cluster_mask = training_clusters == i
                cluster_data = TRAINING_DATA[cluster_mask]
                ax.scatter(
                    cluster_data[:, 0],      # Annual Income (x-axis)
                    cluster_data[:, 1],      # Spending Score (y-axis)
                    c=colors[i % len(colors)],
                    label=f'Cluster {i}',
                    alpha=0.6,               # Transparency
                    s=50                     # Point size
                )
        
        # Plot cluster centers
        # CONCEPT: Centroids represent the "average" customer in each cluster
        ax.scatter(
            CLUSTER_CENTERS[:, 0],
            CLUSTER_CENTERS[:, 1],
            c='black',
            marker='X',
            s=200,
            label='Cluster Centers',
            edgecolors='white',
            linewidths=2
        )
        
        # Highlight the predicted customer point
        # CONCEPT: Emphasize user's input point for clarity
        ax.scatter(
            annual_income,
            spending_score,
            c='yellow',
            marker='*',
            s=500,
            label='Your Customer',
            edgecolors='black',
            linewidths=2,
            zorder=5  # Draw on top
        )
        
        # Customize plot
        ax.set_xlabel(FEATURE_NAMES[0], fontsize=12, fontweight='bold')
        ax.set_ylabel(FEATURE_NAMES[1], fontsize=12, fontweight='bold')
        ax.set_title('Customer Segmentation: K-Means Clustering (k=5)', fontsize=14, fontweight='bold')
        ax.legend(loc='best', framealpha=0.9)
        ax.grid(True, alpha=0.3)
        
        # Display plot in Streamlit
        # CONCEPT: st.pyplot() renders matplotlib figures
        st.pyplot(fig)
        
        # Additional information
        st.info(f'✅ Customer with Annual Income ${annual_income:.1f}k and Spending Score {spending_score:.0f} belongs to **Cluster {cluster_id}**')
        
        # Show cluster center for predicted cluster
        center = CLUSTER_CENTERS[cluster_id]
        st.write(f"**Cluster {cluster_id} Center:**")
        st.write(f"- Average Annual Income: ${center[0]:.2f}k")
        st.write(f"- Average Spending Score: {center[1]:.2f}")

else:
    # Error state: model not loaded
    st.error("⚠️ Model files not found. Please run 'train_customer_model.py' first to generate the model files.")
    st.code("""
# Run this command in your terminal:
python train_customer_model.py
    """, language='bash')
