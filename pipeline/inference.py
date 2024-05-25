import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from pipeline.features import FeatureEngineering
import joblib
from tensorflow.keras.models import load_model

class Inference:
    def __init__(self):
        self.fe = FeatureEngineering()
        self.classes = np.load('../models/classes.npy', allow_pickle=True)
        self.training_columns = ['length', 'num_alpha', 'num_digits', 'prefix_0x',
                                 'prefix_1', 'prefix_3', 'prefix_X', 'prefix_bc1', 'prefix_unknown',
                                 'checksum_base58check', 'checksum_keccak-256', 'checksum_unknown',
                                 'checksum_x11']
        self.scaler = StandardScaler()

        # Load pre-trained models
        self.models = {
            "RandomForest": joblib.load("../models/RandomForest.pkl"),
            "SVC": joblib.load("../models/SVC.pkl"),
            "NaiveBayes": joblib.load("../models/NaiveBayes.pkl")
        }

        # Load neural network model
        self.nn_model = load_model("../models/neural_network_model.keras")

    def preprocess_data(self, address):
        address_features = self.fe.extract_features(address)
        df = pd.DataFrame([address_features])

        # One-hot encode categorical features
        df = pd.get_dummies(df, columns=['prefix', 'checksum'])

        # Add missing columns
        missing_columns = list(set(self.training_columns) - set(df.columns))
        for col in missing_columns:
            df[col] = 0

        # Reorder columns to match training data
        df = df[self.training_columns]
        print(df.columns)

        # Scale features
        df_scaled = self.scaler.fit_transform(df)
        return df_scaled

    def models_inference(self, address):
        df_scaled = self.preprocess_data(address)
        results = {}
        for model_name, model in self.models.items():
            prediction = model.predict(df_scaled)[0]
            predicted_class = self.classes[prediction]
            results[model_name] = predicted_class
        return results

    def nn_inference(self, address):
        address_preprocessed = self.preprocess_data(address)
        prediction = self.nn_model.predict(address_preprocessed)
        predicted_class = np.argmax(prediction, axis=1)
        predicted_label = self.classes[predicted_class][0]
        return predicted_label

# Example usage
if __name__ == "__main__":
    test_address = "1N88Ctk7e3taTxjKwzNKTUU1Jc9QJ99q35"
    inference = Inference()
    
    results = inference.models_inference(test_address)
    print("Inference results for address:", test_address)
    for model_name, predicted_class in results.items():
        print(f"{model_name}: {predicted_class}")

    nn_result = inference.nn_inference(test_address)
    print("Neural Network prediction:", nn_result)