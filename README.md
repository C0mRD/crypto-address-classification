# crypto-address-classification
# Cryptocurrency Address Classification

## Table of Contents
- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Setup Instructions](#setup-instructions)
- [Feature Extraction](#feature-extraction)
- [Model Training](#model-training)
- [Model Performance](#model-performance)
- [Inference](#inference)
- [Future Work](#future-work)

## Project Overview
This project aims to classify cryptocurrency addresses into three types: Bitcoin, Ethereum, and Dash, using machine learning techniques. The classification is based on various features extracted from the addresses.

## Setup Instructions
### Prerequisites
- Python 3.10
- pip

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/your_project.git
    cd your_project
    ```

2. Install the package:
    ```bash
    pip install .
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Feature Extraction
Feature extraction is handled in the `feature.py` file within the `pipeline` directory. Key features include:
- Length of the address
- Number of alphabetic characters
- Number of digits
- Address prefixes (e.g., `0x`, `1`, `3`, `bc1`, `X`, `7`)
- Character set used (alphanumeric, hex, base58, etc.)
- Checksum validation

## Model Training
Model training is performed in the `Training.ipynb` notebook. Various classification models were trained and evaluated, including:
- Logistic Regression
- Random Forest
- Gradient Boosting
- Neural Networks

## Model Performance
Model performance was evaluated using various metrics, including accuracy, precision, recall, and F1 score. The Random Forest model showed the best performance, followed by Gradient Boosting and Logistic Regression.

### Feature Importance
Feature importance was assessed using the feature importances attribute of the Random Forest model. Key features contributing to the model's performance include:
- Address length
- Number of digits
- Prefix type

## Inference
The `inference.py` script is used for making predictions on new addresses. It loads the trained model and the label encoder, extracts features from the input address, preprocesses these features, and then uses the model to predict the address type.

### Usage
1. Ensure the trained model and the label encoder are saved in the `models` directory.
2. Run the `inference.py` script with the address to be classified.

## Future Work
Future enhancements to the project may include:
- Adding support for more cryptocurrency address types
- Improving feature extraction methods
- Exploring advanced machine learning models for better performance
- Implementing a web API for real-time address classification

---

This template provides a clear structure and concise descriptions of each part of your project. You can customize it further as needed to fit the specific details and requirements of your project.

