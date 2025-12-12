# 📖 Key Terms Glossary - Simple One-Line Definitions

## Core Machine Learning Terms

### **Machine Learning (ML)**
A method where computers learn patterns from data to make predictions or decisions without being explicitly programmed for each task.

### **Supervised Learning**
A type of ML where the model learns from labeled data (input-output pairs) to make predictions on new, unseen data.

### **Unsupervised Learning**
A type of ML where the model finds patterns in data without labeled examples, like grouping similar items together.

### **Clustering**
An unsupervised learning technique that groups similar data points together into clusters based on their characteristics.

### **Model**
A mathematical representation trained on data that can make predictions or identify patterns in new data.

### **Training**
The process of teaching a model by showing it data so it can learn patterns and relationships.

### **Inference**
Using a trained model to make predictions or classifications on new, unseen data.

### **Feature**
A measurable property or characteristic of data used as input for machine learning models (like Annual Income or Spending Score).

### **Label**
The correct answer or category for a data point in supervised learning (not used in clustering).

---

## K-Means Clustering Terms

### **K-Means**
An unsupervised clustering algorithm that groups data into k clusters by finding cluster centers (centroids) that minimize distances to data points.

### **Cluster**
A group of data points that are similar to each other and different from points in other groups.

### **Centroid**
The center point of a cluster, calculated as the average (mean) of all points in that cluster.

### **K (Number of Clusters)**
The number of groups you want the algorithm to create (in our case, k=5 customer segments).

### **Distance Metric**
A way to measure how similar or different two data points are (we use Euclidean distance).

### **Euclidean Distance**
The straight-line distance between two points in space, calculated using the Pythagorean theorem.

### **Initialization**
The starting positions of cluster centers before the algorithm begins (k-means++ is a smart initialization method).

### **Convergence**
When the algorithm stops because cluster centers no longer move significantly between iterations.

### **Within-Cluster Sum of Squares (WCSS)**
A measure of how tightly grouped points are within each cluster (lower is better).

### **Assignment Step**
The phase where each data point is assigned to its nearest cluster center.

### **Update Step**
The phase where cluster centers are moved to the average position of all points assigned to them.

---

## Data Science Terms

### **Data Simulation**
Creating synthetic (fake) data that mimics real-world patterns when actual data is unavailable or sensitive.

### **Synthetic Data**
Artificially generated data that has similar statistical properties to real data but doesn't contain real information.

### **Normal Distribution**
A bell-shaped probability distribution where most values cluster around the mean (like income distribution).

### **Uniform Distribution**
A probability distribution where all values in a range have equal likelihood of occurring.

### **Random Seed**
A starting point for random number generation that ensures reproducible results (same seed = same random numbers).

### **Reproducibility**
The ability to get the same results when running code multiple times, crucial for scientific validity.

### **NumPy Array**
A data structure in Python for efficient numerical computations, like a table of numbers.

### **2D Array**
An array with rows and columns, like a spreadsheet (shape: n_samples × n_features).

### **Data Preprocessing**
Cleaning and preparing raw data before feeding it to a machine learning model.

---

## Model Serialization Terms

### **Serialization**
Converting a Python object (like a trained model) into a format that can be stored or transmitted (byte stream).

### **Pickle**
Python's built-in module for serializing objects to binary format for saving to disk.

### **Deserialization**
Converting a serialized object back into its original Python form (loading from disk).

### **Model Persistence**
Saving a trained model to disk so it can be loaded later without retraining.

### **Binary File**
A file format that stores data as bytes (0s and 1s) rather than human-readable text.

### **.pkl File**
A pickle file containing a serialized Python object (like a trained model).

### **Metadata**
Additional information stored alongside the model (like feature names, cluster centers) needed for using the model.

---

## Streamlit Framework Terms

### **Streamlit**
A Python framework that makes it easy to build interactive web applications for machine learning and data science.

### **Widget**
An interactive UI element that lets users input data or interact with the app (like sliders, buttons).

### **Sidebar**
A vertical panel on the side of the Streamlit app, commonly used for input controls.

### **st.title()**
A Streamlit function that displays a large heading at the top of the app.

### **st.sidebar.slider()**
A Streamlit widget that creates an interactive slider for numeric input in the sidebar.

### **st.button()**
A Streamlit widget that creates a clickable button that triggers an action when pressed.

### **st.metric()**
A Streamlit function that displays a key metric prominently with a label, value, and optional delta.

### **st.pyplot()**
A Streamlit function that displays a matplotlib plot in the app.

### **st.dataframe()**
A Streamlit function that displays a pandas DataFrame as an interactive table.

### **st.error()**
A Streamlit function that displays an error message in red.

### **st.info()**
A Streamlit function that displays an informational message in blue.

### **st.success()**
A Streamlit function that displays a success message in green.

### **Reactivity**
The automatic updating of the Streamlit app when user inputs change.

---

## Caching Terms

### **Caching**
Storing computed results in memory to avoid recalculating them on every app interaction.

### **@st.cache_resource**
A Streamlit decorator that caches objects that shouldn't be copied (like models, database connections).

### **@st.cache_data**
A Streamlit decorator that caches data that can be copied (like DataFrames, arrays).

### **Cache Invalidation**
When cached data is cleared and recomputed (happens when code changes or cache is manually cleared).

### **Decorator**
A Python feature that modifies a function's behavior without changing its code (the @ symbol).

---

## Data Visualization Terms

### **Visualization**
Representing data graphically to help understand patterns, trends, and relationships.

### **Scatter Plot**
A graph that displays data points on two axes, useful for showing relationships between two variables.

### **Matplotlib**
A Python library for creating static, animated, and interactive visualizations.

### **Figure**
The entire plotting area in matplotlib, like a blank canvas.

### **Axes**
The actual plot area within a figure where data is drawn (x-axis and y-axis).

### **Color Coding**
Using different colors to distinguish between categories or groups in a visualization.

### **Marker**
The symbol used to represent a data point on a plot (circle, square, star, X, etc.).

### **Alpha (Transparency)**
A value between 0 and 1 that controls how transparent/opaque a plot element is.

---

## Customer Segmentation Terms

### **Customer Segmentation**
The process of dividing customers into groups based on similar characteristics or behaviors.

### **Customer Profile**
A description of a customer's characteristics, behaviors, and preferences.

### **Annual Income**
The total amount of money a customer earns per year (in thousands of dollars for our model).

### **Spending Score**
A numerical rating (1-100) representing how much a customer spends relative to others.

### **Cluster ID**
A number (0 to k-1) assigned to each customer indicating which segment they belong to.

### **Segment**
Another word for cluster - a group of customers with similar characteristics.

---

## Scikit-learn Terms

### **Scikit-learn (sklearn)**
A popular Python library providing machine learning algorithms and tools.

### **KMeans**
The scikit-learn class that implements the K-Means clustering algorithm.

### **fit()**
A method that trains the model on data (learns cluster centers).

### **predict()**
A method that uses a trained model to assign new data points to clusters.

### **cluster_centers_**
An attribute of the trained KMeans model containing the coordinates of each cluster's center.

### **n_clusters**
A parameter specifying how many clusters to create.

### **init='k-means++'**
A smart initialization method that places initial centroids far apart for better results.

### **n_init**
The number of times to run the algorithm with different initializations, keeping the best result.

### **max_iter**
The maximum number of iterations the algorithm will perform before stopping.

---

## NumPy Terms

### **NumPy**
A Python library for numerical computing, providing efficient array operations.

### **np.random.seed()**
A function that sets the starting point for random number generation (ensures reproducibility).

### **np.random.normal()**
A function that generates random numbers from a normal (bell curve) distribution.

### **np.random.uniform()**
A function that generates random numbers uniformly across a range.

### **np.clip()**
A function that limits values to a specified range (clamps values).

### **np.column_stack()**
A function that combines multiple 1D arrays into a 2D array (like stacking columns).

### **np.array()**
A function that creates a NumPy array from a list or other data structure.

---

## Pandas Terms

### **Pandas**
A Python library for data manipulation and analysis, providing DataFrames and Series.

### **DataFrame**
A 2D table-like data structure with rows and columns, similar to a spreadsheet.

### **pd.DataFrame()**
A function that creates a DataFrame from arrays, lists, or dictionaries.

---

## File Operations Terms

### **File Mode**
A specification of how to open a file: 'r' (read), 'w' (write), 'rb' (read binary), 'wb' (write binary).

### **'rb' Mode**
Read binary mode - used for reading pickle files and other binary data.

### **'wb' Mode**
Write binary mode - used for writing pickle files and other binary data.

### **os.path.exists()**
A function that checks if a file or directory exists at a given path.

### **Context Manager (with statement)**
A Python feature that automatically handles file opening/closing and error handling.

---

## Error Handling Terms

### **Exception**
An error that occurs during program execution that interrupts normal flow.

### **try-except Block**
A Python construct that catches and handles exceptions gracefully instead of crashing.

### **Error Message**
A message displayed to the user when something goes wrong, helping them understand the issue.

---

## Real-World Analogy

Think of customer segmentation like organizing a library:

- **Data Points (Customers)** = Individual books in the library
- **Features** = Book characteristics (genre, author, length, publication year)
- **Clustering** = Organizing books into sections (Fiction, Non-Fiction, Science, History, etc.)
- **Centroid** = The "typical" book in each section (average characteristics)
- **K (Number of Clusters)** = Number of sections you want (5 sections = k=5)
- **Training** = The librarian organizing books into sections based on similarities
- **Prediction** = When a new book arrives, determining which section it belongs to
- **Model** = The organizational system the librarian learned
- **Pickle/Serialization** = Writing down the organizational system so other librarians can use it
- **Streamlit App** = A self-service kiosk where people can find which section their book belongs to
- **Visualization** = A map of the library showing where each section is located

---

## Quick Reference: Most Important Terms

1. **K-Means** = Algorithm that groups data into k clusters
2. **Cluster** = A group of similar data points
3. **Centroid** = The center point of a cluster
4. **Feature** = A measurable characteristic of data
5. **Training** = Teaching the model with data
6. **Inference** = Using trained model to make predictions
7. **Pickle** = Saving/loading Python objects to/from disk
8. **Streamlit** = Framework for building ML web apps
9. **Widget** = Interactive UI element (slider, button)
10. **Caching** = Storing results to avoid recomputation
11. **Scatter Plot** = Graph showing relationship between two variables
12. **Serialization** = Converting objects to storable format
13. **Metadata** = Additional information stored with model
14. **Reproducibility** = Getting same results every time
15. **Customer Segmentation** = Grouping customers by similarity

---

## Algorithm Flow: K-Means Step-by-Step

1. **Initialize** = Place k centroids randomly (or using k-means++)
2. **Assign** = Assign each point to nearest centroid
3. **Update** = Move centroids to mean of assigned points
4. **Repeat** = Go back to step 2 until centroids stop moving
5. **Done** = Final clusters and centroids are ready

---

## File Structure Terms

### **Training Script**
A Python file that creates and trains the model (train_customer_model.py).

### **Application Script**
A Python file that creates the user interface (customer_segmentation_app.py).

### **Requirements File**
A text file listing all Python packages needed for the project (requirements.txt).

### **Model File**
A pickle file containing the trained model (.pkl extension).

### **Metadata File**
A pickle file containing additional information about the model (.pkl extension).

---

## Evaluation Terms (Part 2)

### **GEval**
A framework from DeepEval for automated evaluation of LLM applications.

### **LLM-as-a-Judge**
Using a Large Language Model to evaluate the quality of other LLM outputs.

### **Evaluation Metric**
A measure used to assess the quality of a model or system (like accuracy, helpfulness).

### **Plan Quality**
A metric evaluating how good a planning agent's output is.

### **Helpfulness**
A metric measuring how useful and informative an answer is.

### **Improvement Score**
A metric comparing final output to draft to measure enhancement.

### **Correlation ID**
A unique identifier linking related messages across different stages of processing.

---

## Kafka Terms (Part 2)

### **Kafka**
A distributed streaming platform for building real-time data pipelines.

### **Topic**
A category or feed name where messages are published and consumed.

### **Producer**
An application that sends messages to Kafka topics.

### **Consumer**
An application that reads messages from Kafka topics.

### **Message**
A unit of data sent through Kafka (like a task or result).

### **Multi-Agent System**
A system where multiple AI agents work together, each with a specific role.
