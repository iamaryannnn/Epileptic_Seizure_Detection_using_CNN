# 🧠 Epileptic Seizure Detection using CNN

This project implements a Convolutional Neural Network (CNN) to classify EEG data for epileptic seizure detection. It uses the publicly available **Epileptic Seizure Recognition** dataset from the UCI repository (via GitHub mirror).

## 📁 Project Structure

```
EPILEPTIC_SEIZURE_CNN.ipynb     # Jupyter Notebook with preprocessing, model, and evaluation
app.py                          # Streamlit web app for live testing
README.md                       # Project documentation
```

## 📊 Dataset

- **Source:** [Epileptic Seizure Recognition Dataset](https://github.com/mohsin-riad/Epileptic-Seizure-Recognition)
- **Format:** CSV with 178 time-series features + label (`y`)
- **Classes:** 
  - `1` = Seizure
  - `0` = Non-Seizure (converted from original classes 2–5)

## 🛠️ Requirements

```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow streamlit
```

## 🚀 How to Use

1. Run the notebook to train the model: `EPILEPTIC_SEIZURE_CNN.ipynb`
2. Save the model (`cnn_seizure_model.h5`)
3. Launch the Streamlit app:

```bash
streamlit run app.py
```

4. Upload a `.csv` EEG sample with 178 columns
5. View prediction results

## 🧠 Model Architecture

- 1D Convolution Layers (Conv1D)
- Max Pooling
- Flatten + Dense Layers
- Dropout regularization
- Sigmoid activation for binary classification

## 🏁 Future Improvements

- Add CNN+LSTM model
- Export model to `.tflite` for mobile use
- Host web app on Streamlit Cloud

---
Made for academic/project use. Not for clinical diagnosis.
