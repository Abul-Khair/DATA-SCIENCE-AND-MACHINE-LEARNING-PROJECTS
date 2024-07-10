import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# Title of the web app
st.title('Iris Dataset Classification')

# Description
st.write("""
This web app predicts the **Iris flower** species based on input parameters.
""")

# Sidebar - Input parameters
st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal length (cm)': sepal_length,
            'sepal width (cm)': sepal_width,
            'petal length (cm)': petal_length,
            'petal width (cm)': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target

# Build a Random Forest Classifier
rfc = RandomForestClassifier()
rfc.fit(X, Y)

# Get user input
df = user_input_features()

# Display user input
st.subheader('User Input parameters:')
st.write(df)

# Predicting the output
prediction = rfc.predict(df)
prediction_proba = rfc.predict_proba(df)

# Displaying the prediction
st.subheader('Class Labels and their corresponding index number:')
st.write(iris.target_names)

st.subheader('Prediction:')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probability:')
st.write(prediction_proba)
