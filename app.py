from flask import Flask, render_template, request, jsonify
import numpy as np
import time
from sklearn.preprocessing import StandardScaler
import random
app = Flask(__name__)

# Variable to keep track of time for sinusoidal data generation
start_time = time.time()

# Function to generate sinusoidal data
def generate_sinusoidal_data():
    current_time = time.time() - start_time
    value = 50 + 50 * np.sin(current_time)
    return value

# Function to extract features from the website link (dummy function)
def extract_features(website_link):
    url_length = len(website_link)
    return np.array([[url_length] * 10])

# Function to preprocess input data (dummy function)
def preprocess_data(data):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    return scaler.fit_transform(data)

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        website_link = request.form['website_link']

        # Example of feature extraction and preprocessing (replace with actual logic)
        features = extract_features(website_link)
        features = np.reshape(features, (1, -1))
        features = preprocess_data(features)

        # Dummy prediction logic
        is_ddos_attack = random.random() > 0.5

        # Render result template with data
        return render_template('result.html', website_link=website_link, is_ddos_attack=is_ddos_attack)

    return render_template('index.html')

# Route to provide live network traffic data (sinusoidal function)
@app.route('/get_live_network_traffic_data')
def get_live_network_traffic_data():
    value = generate_sinusoidal_data()
    return jsonify({'value': value})

if __name__ == '__main__':
    app.run(debug=True)
