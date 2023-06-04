from flask import Flask, jsonify, request
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/correlation', methods=['POST'])
def calculate_correlation():
    # Retrieve data from request
    data = request.get_json()

    # Validate and preprocess data if needed
    # Assuming the data is in the format: { "x": [1, 2, 3, ...], "y": [4, 5, 6, ...] }

    # Check if required fields are present
    if 'x' not in data or 'y' not in data:
        return jsonify({'error': 'Missing data fields'}), 400

    # Convert data to pandas DataFrame
    df = pd.DataFrame(data)

    # Check for any missing values and handle as needed
    if df.isnull().values.any():
        return jsonify({'error': 'Missing values detected in the data'}), 400

    # Perform correlation calculation
    correlation = df['x'].corr(df['y'])

    # Prepare response
    response = {
        'correlation': correlation
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
