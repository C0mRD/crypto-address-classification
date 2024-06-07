import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re

# Load the trained model
model = load_model('models/crypto_address_classifier_epoch1_newv2.h5')

# Load the tokenizer
with open('models/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Load the label encoder
with open('models/label_encoder.pickle', 'rb') as handle:
    label_encoder = pickle.load(handle)

# Load max_length from the text file
with open('models/max_length.txt', 'r') as f:
    max_length = int(f.read())

# Define regex patterns for each cryptocurrency
regex_patterns = {
    'bitcoin': r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$|^bc1[ac-hj-np-z02-9]{38,59}$',
    'ethereum': r'^0x[a-fA-F0-9]{40}$',
    'dash': r'^X[1-9A-HJ-NP-Za-km-z]{33}$',
    'tron': r'^T[a-zA-Z0-9]{33}$',
    'monero': r'^[48][a-z0-9]{94}$'
}

def nn_prediction(address):
    # Preprocess the address
    sequence = tokenizer.texts_to_sequences([address])
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding='post')

    # Predict the class for the address
    prediction = model.predict(padded_sequence)
    predicted_class = prediction.argmax(axis=-1)
    predicted_label = label_encoder.inverse_transform(predicted_class)
    return predicted_label[0]

def combined_prediction(address):
    # Preprocess the address
    sequence = tokenizer.texts_to_sequences([address])
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding='post')

    # Predict the class for the address
    prediction = model.predict(padded_sequence)
    predicted_class = prediction.argmax(axis=-1)
    predicted_label = label_encoder.inverse_transform(predicted_class)[0]

    # Convert the predicted label to lowercase to match the regex dictionary
    predicted_label_lower = predicted_label.lower()

    # Check the address with regex patterns
    matched_label = None
    for label, pattern in regex_patterns.items():
        if re.match(pattern, address):
            matched_label = label.lower()
            break

    # Compare model prediction with regex match
    if matched_label == predicted_label_lower:
        return predicted_label
    else:
        return 'unknown'