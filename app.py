import streamlit as st
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np

# Load model
model = load_model("cnn_seizure_model.h5")

st.title("🧠 Epileptic Seizure Detection")
st.markdown("Upload a CSV file with 178 EEG features to predict seizure activity.")

uploaded_file = st.file_uploader("Choose your EEG .csv file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data Preview:")
    st.write(data.head())

    # Make sure it's the right shape
    if data.shape[1] == 178:
        input_data = data.values.reshape(data.shape[0], data.shape[1], 1)
        prediction = model.predict(input_data)
        binary = (prediction > 0.5).astype(int)

        st.write("Predictions:")
        for i, pred in enumerate(binary):
            label = "⚠️ Seizure" if pred[0] == 1 else "✅ No Seizure"
            st.write(f"Sample {i+1}: {label}")
    else:
        st.error("Uploaded CSV must have exactly 178 columns.")
