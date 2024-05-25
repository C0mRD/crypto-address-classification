import pandas as pd

class Preprocessing:
    def __init__(self, btc_path, eth_path, dash_path):
        self.btc_data = pd.read_csv(btc_path)
        self.eth_data = pd.read_csv(eth_path)
        self.dash_data = pd.read_csv(dash_path)

    def clean_data(self):
        # Remove duplicate rows
        self.btc_data = self.btc_data.drop_duplicates()
        self.eth_data = self.eth_data.drop_duplicates()
        self.dash_data = self.dash_data.drop_duplicates()

        # Remove leading and trailing whitespaces
        self.data['address'] = self.data['address'].str.strip()

    def take_address(self):
        # Take only necessary address column
        self.btc_address = self.btc_data['address'].copy()
        self.eth_address = self.eth_data['address'].copy()
        self.dash_address = self.dash_data['address'].copy()

    def add_label(self):
        self.btc_address['type'] = 'bitcoin'
        self.eth_address['type'] = 'ethereum'
        self.dash_address['type'] = 'dash'

    def combine_data(self):
        self.data = pd.concat([self.btc_address, self.eth_address, self.dash_address], ignore_index=True)

    def get_data(self):
        self.data = self.data.sample(frac=1).reset_index(drop=True).copy()
        return self.data