import pandas as pd
import re

class FeatureEngineering:
    def __init__(self, data=None):
        self.data = data

    def extract_features(self, address):
        features = {}
    
        # Length of the address
        features['length'] = len(address)
    
        # Prefix of the address
        if address.startswith('0x'):
            features['prefix'] = '0x'
        elif address.startswith('1'):
            features['prefix'] = '1'
        elif address.startswith('3'):
            features['prefix'] = '3'
        elif address.startswith('bc1'):
            features['prefix'] = 'bc1'
        elif address.startswith('X'):
            features['prefix'] = 'X'
        else:
            features['prefix'] = 'unknown'

        # Checksum mechanism
        if re.match(r'^0x[a-fA-F0-9]{40}$', address):
            features['checksum'] = 'keccak-256'
        elif re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address) or re.match(r'^bc1[ac-hj-np-z02-9]{38,59}$', address):
            features['checksum'] = 'base58check'
        elif re.match(r'^X[1-9A-HJ-NP-Za-km-z]{25,34}$', address):
            features['checksum'] = 'x11'
        else:
            features['checksum'] = 'unknown'
    
        # Number of alphabetic characters and digits
        features['num_alpha'] = sum(c.isalpha() for c in address)
        features['num_digits'] = sum(c.isdigit() for c in address)
    
        return features
    
    def create_features(self):
        # Extract features for the dataset
        df_features = self.data['address'].apply(self.extract_features)
        df_features = pd.json_normalize(df_features)
        self.data = pd.concat([self.data, df_features], axis=1)
        return self.data