# HW10: Customer Segmentation with K-Means Clustering

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Model
```bash
python train_customer_model.py
```

This will create:
- `customer_kmeans_model_yourname.pkl` (trained model)
- `customer_metadata.pkl` (metadata for the app)

**Important:** Replace `yourname` in the filename with your actual name before submission!

### 3. Run the Streamlit App
```bash
streamlit run customer_segmentation_app.py
```

The app will open in your browser automatically.

## Files Overview

- **train_customer_model.py**: Trains K-Means model and saves it
- **customer_segmentation_app.py**: Streamlit web application
- **requirements.txt**: Python dependencies
- **HW10_CONCEPTS_EXPLAINED.md**: Detailed concept explanations

## What This Does

1. **Simulates** 200 customer records with:
   - Annual Income (15k - 140k)
   - Spending Score (1 - 100)

2. **Trains** a K-Means clustering model with 5 clusters

3. **Creates** an interactive web app where you can:
   - Input customer parameters via sliders
   - Predict which cluster the customer belongs to
   - Visualize the customer on a scatter plot

## Key Concepts Covered

- K-Means Clustering (unsupervised learning)
- Model Serialization (pickle)
- Streamlit Framework (web apps)
- Data Visualization (matplotlib)
- Caching (@st.cache_resource)

For detailed explanations, see **HW10_CONCEPTS_EXPLAINED.md**.

## Submission Requirements

1. ✅ `customer_kmeans_model_yourname.pkl`
2. ✅ Screenshot of running Streamlit application

## Troubleshooting

**Error: Model files not found**
- Make sure you ran `train_customer_model.py` first
- Check that `.pkl` files are in the same directory as the app

**Error: Module not found**
- Run `pip install -r requirements.txt`
- Make sure you're using Python 3.8+

**App won't start**
- Check that Streamlit is installed: `pip install streamlit`
- Try: `python -m streamlit run customer_segmentation_app.py`
