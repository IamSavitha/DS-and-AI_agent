# HW10: Customer Segmentation - Complete Concept Explanation

## Table of Contents
1. [Overview](#overview)
2. [Part 1: Customer Segmentation](#part-1-customer-segmentation)
3. [Core Concepts Explained](#core-concepts-explained)
4. [Code Walkthrough](#code-walkthrough)
5. [Part 2: Kafka Agents Evaluation](#part-2-kafka-agents-evaluation)

---

## Overview

This homework covers two main topics:
- **Part 1**: Building a customer segmentation system using K-Means clustering and Streamlit
- **Part 2**: Evaluating Kafka-based multi-agent systems using GEval

---

## Part 1: Customer Segmentation

### What is Customer Segmentation?

**Customer Segmentation** is the process of dividing customers into groups (clusters) based on similar characteristics. This helps businesses:
- Target marketing campaigns more effectively
- Understand customer behavior patterns
- Personalize products and services
- Optimize pricing strategies

### The K-Means Algorithm

**K-Means Clustering** is an unsupervised machine learning algorithm that:
- Groups data points into k clusters
- Minimizes the sum of squared distances from points to cluster centers
- Works iteratively to find optimal cluster assignments

**Key Concepts:**
- **Centroid**: The center point of a cluster (mean of all points in cluster)
- **Distance Metric**: Usually Euclidean distance
- **Convergence**: Algorithm stops when centroids no longer move significantly

---

## Core Concepts Explained

### 1. Data Simulation

**What is it?**
Creating synthetic data that mimics real-world patterns when actual data is unavailable or sensitive.

**Why use it?**
- Privacy: Real customer data is sensitive
- Reproducibility: Same seed = same data
- Testing: Validate algorithms before production
- Education: Demonstrate concepts without real data

**How it works:**
```python
# Normal distribution for Annual Income
annual_income = np.random.normal(loc=60, scale=15, size=200)
```
- `loc=60`: Mean income of $60k
- `scale=15`: Standard deviation of $15k
- Creates realistic income distribution

**Real-world analogy:** Like creating a mock dataset of customer profiles for testing before using real customer data.

---

### 2. K-Means Clustering Algorithm

**Step-by-step process:**

1. **Initialization**: Randomly place k centroids
2. **Assignment**: Assign each point to nearest centroid
3. **Update**: Move centroids to mean of assigned points
4. **Repeat**: Steps 2-3 until convergence

**Mathematical foundation:**
- **Objective function**: Minimize within-cluster sum of squares (WCSS)
- **Distance formula**: Euclidean distance: √[(x₂-x₁)² + (y₂-y₁)²]
- **Centroid update**: Mean of all points in cluster

**Key parameters:**
- `n_clusters=5`: Number of customer segments
- `init='k-means++'`: Smart initialization (better than random)
- `n_init=10`: Run 10 times, pick best result
- `max_iter=300`: Maximum iterations per run

**Why k=5?**
- Common practice: 3-7 segments are manageable
- Too few: Overly broad segments
- Too many: Over-segmentation, hard to interpret

---

### 3. Model Serialization (Pickling)

**What is serialization?**
Converting Python objects into byte streams for storage/transmission.

**Why pickle models?**
- **Persistence**: Save trained models to disk
- **Deployment**: Load models in production without retraining
- **Efficiency**: Training can take hours; loading takes seconds
- **Versioning**: Track different model versions

**How it works:**
```python
# Save
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Load
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
```

**Security note:** Only unpickle files from trusted sources! Pickle can execute arbitrary code.

**File modes:**
- `'wb'`: Write binary (for saving)
- `'rb'`: Read binary (for loading)

---

### 4. Metadata Management

**What is metadata?**
Additional information stored alongside the model that's needed for inference.

**Why store metadata?**
- **Feature names**: What each column represents
- **Cluster centers**: For visualization and analysis
- **Training data**: For plotting in the app
- **Configuration**: Model parameters, version info

**Example metadata structure:**
```python
metadata = {
    'feature_names': ['Annual Income (k$)', 'Spending Score (1-100)'],
    'cluster_centers': array([[...], [...], ...]),
    'n_clusters': 5,
    'training_data': array([...])
}
```

**Best practice:** Store everything needed to use the model without referring back to training code.

---

### 5. Streamlit Framework

**What is Streamlit?**
A Python framework for building web apps for machine learning and data science.

**Key features:**
- **Simple syntax**: Python functions create UI elements
- **Automatic reactivity**: App updates when inputs change
- **Built-in widgets**: Sliders, buttons, charts, etc.
- **No frontend knowledge needed**: Pure Python

**Why use Streamlit?**
- **Rapid prototyping**: Build apps in minutes, not days
- **Interactive demos**: Show ML models to stakeholders
- **Data exploration**: Interactive data analysis tools
- **Model deployment**: Quick way to deploy models

**Core components:**
- `st.title()`: Main heading
- `st.sidebar`: Sidebar container
- `st.slider()`: Numeric input widget
- `st.button()`: Clickable button
- `st.metric()`: Display key metrics
- `st.pyplot()`: Show matplotlib plots

---

### 6. Caching with @st.cache_resource

**What is caching?**
Storing computed results to avoid recomputation.

**Why cache model loading?**
- **Performance**: Loading models is slow (disk I/O)
- **User experience**: Instant app startup after first load
- **Resource efficiency**: Don't reload on every interaction

**How @st.cache_resource works:**
```python
@st.cache_resource
def load_model():
    # This code runs ONCE
    # Results cached in memory
    # Subsequent calls return cached result
    return model
```

**Cache types:**
- `@st.cache_data`: For data (DataFrames, arrays) - can be copied
- `@st.cache_resource`: For resources (models, DB connections) - shouldn't be copied

**Cache invalidation:**
- Function code changes → cache clears
- User clicks "Clear cache" → cache clears
- App restarts → cache clears

---

### 7. Model Inference

**What is inference?**
Using a trained model to make predictions on new data.

**Inference process:**
1. **Prepare input**: Format data correctly (2D array for sklearn)
2. **Call predict()**: Model assigns cluster ID
3. **Interpret result**: Map cluster ID to business meaning

**Code example:**
```python
# Input: [Annual Income, Spending Score]
input_features = np.array([[60.0, 50.0]])

# Predict: Returns cluster ID (0-4)
cluster_id = model.predict(input_features)[0]
```

**Why 2D array?**
- sklearn expects shape: `(n_samples, n_features)`
- Even single prediction: `[[feature1, feature2]]`
- Batch prediction: `[[f1, f2], [f1, f2], ...]`

---

### 8. Data Visualization

**Why visualize?**
- **Understanding**: See where input falls in data space
- **Validation**: Verify model makes sense
- **Communication**: Explain results to stakeholders
- **Debugging**: Identify issues with model

**Scatter plot components:**
- **Training data points**: Colored by cluster
- **Cluster centers**: Black X markers
- **User's point**: Yellow star (highlighted)
- **Axes**: Annual Income (x), Spending Score (y)

**Color coding:**
- Different colors for each cluster
- Helps distinguish groups visually
- Improves interpretability

---

## Code Walkthrough

### train_customer_model.py - Line by Line

```python
import numpy as np
from sklearn.cluster import KMeans
import pickle
import os
```
**Explanation:** Import necessary libraries
- `numpy`: Numerical operations
- `sklearn.cluster.KMeans`: K-Means implementation
- `pickle`: Serialization
- `os`: File operations

```python
def simulate_customer_data(n_samples=200, random_state=42):
    np.random.seed(random_state)
```
**Explanation:** Set random seed for reproducibility. Same seed = same data every run.

```python
    annual_income = np.random.normal(loc=60, scale=15, size=n_samples)
    annual_income = np.clip(annual_income, 15, 140)
```
**Explanation:**
- Generate income from normal distribution (mean=60k, std=15k)
- Clip to realistic range (15k-140k)

```python
    spending_score = np.random.uniform(low=1, high=100, size=n_samples)
```
**Explanation:** Generate spending scores uniformly across 1-100 range.

```python
    data = np.column_stack([annual_income, spending_score])
    return data
```
**Explanation:** Combine two 1D arrays into 2D array (200 rows × 2 columns).

```python
def train_kmeans_model(data, n_clusters=5, random_state=42):
    model = KMeans(
        n_clusters=n_clusters,
        init='k-means++',
        n_init=10,
        max_iter=300,
        random_state=random_state
    )
```
**Explanation:**
- `n_clusters=5`: Create 5 customer segments
- `init='k-means++'`: Smart initialization (better than random)
- `n_init=10`: Run 10 times, pick best result
- `max_iter=300`: Max iterations per run
- `random_state`: Reproducible results

```python
    model.fit(data)
    return model
```
**Explanation:** Train model on data. `fit()` learns cluster centers.

```python
def save_model_and_metadata(model, data, model_filename, metadata_filename):
    with open(model_filename, 'wb') as f:
        pickle.dump(model, f)
```
**Explanation:**
- `'wb'`: Write binary mode
- `pickle.dump()`: Serialize model to file

```python
    metadata = {
        'feature_names': ['Annual Income (k$)', 'Spending Score (1-100)'],
        'cluster_centers': model.cluster_centers_,
        'n_clusters': model.n_clusters,
        'training_data': data
    }
```
**Explanation:** Create dictionary with all information needed for app.

---

### customer_segmentation_app.py - Line by Line

```python
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
```
**Explanation:** Import libraries for web app, data handling, and visualization.

```python
@st.cache_resource
def load_resources(model_file, metadata_file):
```
**Explanation:** Decorator caches function results. Model loads once, cached for subsequent calls.

```python
    if not os.path.exists(model_file) or not os.path.exists(metadata_file):
        st.error("Required model or metadata files not found...")
        return None, None
```
**Explanation:** Check if files exist before loading. Show error if missing.

```python
    with open(model_file, 'rb') as f:
        model = pickle.load(f)
```
**Explanation:**
- `'rb'`: Read binary mode
- `pickle.load()`: Deserialize model from file

```python
st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="👥",
    layout="wide"
)
```
**Explanation:** Configure app appearance (browser tab title, icon, layout).

```python
model, metadata = load_resources(MODEL_FILE, METADATA_FILE)
```
**Explanation:** Load model and metadata (cached after first call).

```python
annual_income = st.sidebar.slider(
    FEATURE_NAMES[0],
    15.0, 140.0, 60.0, 1.0
)
```
**Explanation:**
- `st.sidebar`: Place in sidebar
- `slider()`: Create interactive slider
- Parameters: label, min, max, default, step

```python
input_features = np.array([[annual_income, spending_score]])
```
**Explanation:** Convert user input to 2D array format required by sklearn.

```python
if st.button('🔮 Predict Customer Cluster', type='primary'):
    cluster_id = model.predict(input_features)[0]
```
**Explanation:**
- `st.button()`: Create clickable button
- `model.predict()`: Get cluster assignment
- `[0]`: Extract single prediction from array

```python
st.metric(
    label="**Predicted Cluster ID**",
    value=f"Cluster {cluster_id}",
    delta=f"Out of {model.n_clusters} clusters"
)
```
**Explanation:** Display metric prominently with label, value, and delta.

```python
fig, ax = plt.subplots(figsize=(10, 6))
```
**Explanation:** Create matplotlib figure and axes for plotting.

```python
for i in range(model.n_clusters):
    cluster_mask = training_clusters == i
    cluster_data = TRAINING_DATA[cluster_mask]
    ax.scatter(cluster_data[:, 0], cluster_data[:, 1], ...)
```
**Explanation:**
- Filter data by cluster
- Plot each cluster with different color
- `[:, 0]`: All rows, column 0 (Annual Income)
- `[:, 1]`: All rows, column 1 (Spending Score)

```python
ax.scatter(annual_income, spending_score, c='yellow', marker='*', s=500, ...)
```
**Explanation:** Highlight user's input point with yellow star.

```python
st.pyplot(fig)
```
**Explanation:** Display matplotlib figure in Streamlit app.

---

## Part 2: Kafka Agents Evaluation

### Overview

Extend the three-agent Kafka system from HW8 (Planner → Writer → Reviewer) with automated evaluation using GEval.

### Concepts

**GEval (DeepEval Framework):**
- Automated evaluation framework for LLM applications
- Uses LLM-as-a-judge pattern
- Evaluates quality, helpfulness, improvement

**Evaluation Metrics:**
1. **Plan Quality**: How good is the Planner's plan?
2. **Helpfulness**: Are Writer and Reviewer answers helpful?
3. **Final-vs-Draft Improvement**: Did Reviewer improve the draft?

**LLM-as-a-Judge:**
- Use an LLM (like Ollama models) to evaluate outputs
- Provides consistent, automated evaluation
- Can evaluate multiple dimensions simultaneously

### Implementation Steps

1. **Setup GEval**: Install DeepEval framework
2. **Create Evaluator**: Script that consumes from Kafka topics
3. **Link Messages**: Use correlation_id to link related messages
4. **Run Evaluation**: Use GEval to score each stage
5. **Display Results**: Show scores for each metric

---

## Summary

### Key Takeaways

1. **K-Means Clustering**: Unsupervised learning for customer segmentation
2. **Model Serialization**: Save/load models with pickle
3. **Streamlit**: Rapid ML app development
4. **Caching**: Optimize performance with @st.cache_resource
5. **Visualization**: Communicate results effectively
6. **Evaluation**: Measure agent system quality with GEval

### Real-World Applications

- **E-commerce**: Segment customers for targeted marketing
- **Banking**: Risk assessment and customer profiling
- **Retail**: Inventory management and pricing strategies
- **Healthcare**: Patient segmentation for personalized care
- **Finance**: Fraud detection and credit scoring

---

## Running the Application

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Train the Model
```bash
python train_customer_model.py
```

### Step 3: Run Streamlit App
```bash
streamlit run customer_segmentation_app.py
```

### Step 4: Interact with App
- Adjust sliders in sidebar
- Click "Predict Customer Cluster"
- View results and visualization

---

## References

- Scikit-learn Documentation: https://scikit-learn.org/
- Streamlit Documentation: https://docs.streamlit.io/
- K-Means Algorithm: https://en.wikipedia.org/wiki/K-means_clustering
- DeepEval Framework: https://github.com/confident-ai/deepeval

---

**Note:** Remember to replace 'yourname' in the model filename with your actual name before submission!
