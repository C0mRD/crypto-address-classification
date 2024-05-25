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

## Deployment
Trained models are deployed as an API service using Fastapi. You can directly try it out here: [https://crypto-address-classification.onrender.com] (https://crypto-address-classification.onrender.com)

## Setup Instructions
### Prerequisites
- Python 3.10
- pip

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/C0mRD/crypto-address-classification.git
    cd crypto-address-classification
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. For Inference:
    ```bash
    cd pipeline
    python inference.py
    ```

## Dataset
I couldn't find any single dataset that contains proper address of multiple crypto currencies. So, I have collected data from different sources.
- [MBal 10m crypto address dataset] (https://www.kaggle.com/datasets/yidongchaintoolai/mbal-10m-crypto-address-label-dataset)
- [Blockchair Dash address dataset] (https://gz.blockchair.com/dash/addresses)

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
- Random Forest
- Support Vector Machine
- Naive Bayes
- Neural Networks

## Model Performance
Model performance was evaluated using various metrics, including accuracy, precision, recall, and F1 score. The Neural Network showed the best performance followed by Random Forest.

| Model Name  | Train Accuracy  |
| :------------ |:---------------:|
| Neural Network | 99.14% |
| Random Forest | 98.35% |
| SVM      |      97.85%   |
| Naive Bayes | 97.34%        |

### Feature Importance
Feature importance was assessed using the feature importances attribute of the Random Forest model. Key features contributing to the model's performance include:
- CheckSum type
- Address length
- Number of digits
- Prefix type
![Feature Imp Image](https://github.com/C0mRD/crypto-address-classification/blob/main/Feature_Engineering/feature_imp.png?raw=true)

## Inference
The `inference.py` script is used for making predictions on new addresses. It loads the trained model and the label encoder, extracts features from the input address, preprocesses these features, and then uses the model to predict the address type.

### Usage
1. Ensure the trained model and the label encoder are saved in the `models` directory.
2. Run the `inference.py` script with the address to be classified.

## Future Work
Future enhancements to the project may include:
- Adding support for more cryptocurrency address types
- Improving feature extraction methods
- Increasing amount of dataset for model training

