# DigitRecognitionML
This project classifies handwritten digits using machine learning models. Models were trained on the MNIST dataset and tested on other datasets then a model was trained on an merged dataset. Detailed information on model training, testing, and evaluation can be found in the Digit Recognizer.pdf located in the docs folder.

## Datasets
MNIST: Used for training and testing.
EMNIST, USPS, SVHN: Used for testing generalization.

## Web App
A web app built using Streamlit allows users to upload or draw digits for prediction. The K-Nearest Neighbors (KNN) model, which performed the best and trained with a merged datasetis used for predictions.

## How to Run
- Install the required dependencies using requirements.txt.
- Run "DigitClassifier.ipynb" for model training (if needed).
- Run "WebApp.ipynb" (if needed).
- Run the Streamlit app:

```bash
pip install -r requirements.txt
streamlit run app.py
```
