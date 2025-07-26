🧠 Epileptic Seizure Detection using CNN
Description
This project utilizes a 1D Convolutional Neural Network (CNN) to classify epileptic seizures from EEG (electroencephalogram) time-series data. The model is built with TensorFlow/Keras and trained on the "Epileptic Seizure Recognition" dataset to distinguish between seizure and non-seizure activity, achieving high accuracy in detection.

Table of Contents
Installation

Usage

Dataset

Model Architecture

Results

Contributing

License

Installation
To set up the project locally, follow these steps:

Clone the repository:

git clone https://github.com/iamaryannnn/Epileptic_Seizure_Detection_using_CNN.git
cd your-repository

Install the required Python libraries:

pip install pandas numpy matplotlib seaborn scikit-learn tensorflow

Usage
You can run the project using the provided Jupyter Notebook (EPILEPTIC_SEIZURE_CNN.ipynb).

Launch Jupyter Notebook:

jupyter notebook

Open EPILEPTIC_SEIZURE_CNN.ipynb.

Make sure to update the file path in the notebook to point to your local copy of the dataset:

# Update this path in Step 2 of the notebook
file_path = r"path/to/your/Epileptic Seizure Recognition.csv"

Run the cells sequentially to load the data, build the model, train it, and evaluate its performance.

Dataset
The model is trained on the "Epileptic Seizure Recognition" dataset. This dataset contains 11,500 samples of EEG recordings, each with 178 data points representing a one-second time window. The target variable y indicates the presence of a seizure (1) or its absence (0).

Model Architecture
The model is a Sequential 1D CNN built with Keras:

Layer (type)

Output Shape

Param #

conv1d (Conv1D)

(None, 176, 32)

128

max_pooling1d (MaxPooling1D)

(None, 88, 32)

0

conv1d_1 (Conv1D)

(None, 86, 64)

6,208

max_pooling1d_1 (MaxPooling1D)

(None, 43, 64)

0

flatten (Flatten)

(None, 2752)

0

dense (Dense)

(None, 64)

176,192

dropout (Dropout)

(None, 64)

0

dense_1 (Dense)

(None, 1)

65

Total params: 182,593





Results
The model achieves a high level of accuracy in classifying seizures. The final evaluation on the test set shows:

Accuracy: ~96%

Classification Report:

              precision    recall  f1-score   support

           0       0.99      0.96      0.97      1835
           1       0.86      0.96      0.91       465

    accuracy                           0.96      2300
   macro avg       0.93      0.96      0.94      2300
weighted avg       0.96      0.96      0.96      2300

Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
