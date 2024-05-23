import pandas as pd
import re

class FeatureEngineering:
    def __init__(self, data):
        self.data = data

    def extract_features(self, address):
        features = {}
        features['length'] = len(address)
        features['num_digits'] = sum(c.isdigit() for c in address)
        features['num_letters'] = sum(c.isalpha() for c in address)
    
        # Character frequency (assuming ASCII characters)
        for char in '0123456789abcdefghijklmnopqrstuvwxyz':
            features[f'char_freq_{char}'] = address.count(char)
    
        # Prefix analysis
        features['starts_with'] = address[0]
        features['ends_with'] = address[-1]
    
        # Specific blockchain patterns
        features['is_btc'] = int(re.match(r'^1|3|bc1', address) is not None)
        features['is_eth'] = int(re.match(r'^0x', address) is not None)
        features['is_dash'] = int(re.match(r'^X', address) is not None)
    
        return features
    
    def create_features(self):
        # Extract features for the dataset
        df_features = self.data['address'].apply(self.extract_features)
        df_features = pd.json_normalize(df_features)
        self.data = pd.concat([self.data, df_features], axis=1)
        return self.data