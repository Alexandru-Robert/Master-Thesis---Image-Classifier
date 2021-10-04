import streamlit as st
import json
import numpy as np

def load_model():
    with open('model.json', 'r') as file:
        data = json.load(file)
    return data


data = load_model()


def show_predict_page():
    st.title("Image Classifier")

    st.write("""### Upload an image to have it classified""")

    classes = (
        "lifestyle",
        "soccer",

    )

    image = st.
    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)

    expericence = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")