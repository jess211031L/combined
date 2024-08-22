from flask import Flask, request, render_template
from pycaret.anomaly import load_model, predict_model
from joblib import load
import pandas as pd
import zipfile
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained models
anomaly_model = load_model('models/anomaly_detection_model')
classification_model = load_model('models/mushroom_classification_model')

# Define the home route for fillbird
@app.route('/')
def home():
    return render_template('fillbird.html')

# Define the prediction route for fillbird
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    input_data = {
        'FISCAL_YR': request.form.get('fiscal_year'),
        'FISCAL_MTH': request.form.get('fiscal_month'),
        'DEPT_NAME': request.form.get('dept_name'),
        'DIV_NAME': request.form.get('div_name'),
        'CAT_DESC': request.form.get('cat_desc'),
        'AMT': request.form.get('amt')
    }

    # Convert the input data into a DataFrame
    input_df = pd.DataFrame([input_data])

    # Ensure the AMT column is in numeric format, replacing errors with NaN
    input_df['AMT'] = pd.to_numeric(input_df['AMT'], errors='coerce')

    # Generate predictions
    predictions = predict_model(anomaly_model, data=input_df)
    anomaly_flag = predictions['Anomaly_Score'][0]

    # Convert numerical prediction to "Anomaly" or "Not Anomaly"
    prediction = "Anomaly" if anomaly_flag > 0 else "Not Anomaly"

    # Return the result to the template
    return render_template('fillbird.html', prediction=prediction)

# Define the home route for the classification model
@app.route('/mushroom')
def mushroom_home():
    return render_template('jess_index.html')

# Define the prediction route for the mushroom classification
@app.route('/mushroom/predict', methods=['POST'])
def mushroom_predict():
    # Collect input data from the form
    cap_shape = request.form.get('cap_shape')
    cap_surface = request.form.get('cap_surface')
    cap_color = request.form.get('cap_color')
    bruises = request.form.get('bruises')
    odor = request.form.get('odor')
    gill_attachment = request.form.get('gill_attachment')
    gill_spacing = request.form.get('gill_spacing')
    gill_size = request.form.get('gill_size')
    gill_color = request.form.get('gill_color')
    stalk_shape = request.form.get('stalk_shape')
    stalk_root = request.form.get('stalk_root')
    stalk_surface_above_ring = request.form.get('stalk_surface_above_ring')
    stalk_surface_below_ring = request.form.get('stalk_surface_below_ring')
    stalk_color_above_ring = request.form.get('stalk_color_above_ring')
    stalk_color_below_ring = request.form.get('stalk_color_below_ring')
    veil_type = request.form.get('veil_type')
    veil_color = request.form.get('veil_color')
    ring_number = request.form.get('ring_number')
    ring_type = request.form.get('ring_type')
    spore_print_color = request.form.get('spore_print_color')
    population = request.form.get('population')
    habitat = request.form.get('habitat')

    # Convert the data into a DataFrame
    input_data = pd.DataFrame({
        'cap_shape': [cap_shape],
        'cap_surface': [cap_surface],
        'cap_color': [cap_color],
        'bruises': [bruises],
        'odor': [odor],
        'gill_attachment': [gill_attachment],
        'gill_spacing': [gill_spacing],
        'gill_size': [gill_size],
        'gill_color': [gill_color],
        'stalk_shape': [stalk_shape],
        'stalk_root': [stalk_root],
        'stalk_surface_above_ring': [stalk_surface_above_ring],
        'stalk_surface_below_ring': [stalk_surface_below_ring],
        'stalk_color_above_ring': [stalk_color_above_ring],
        'stalk_color_below_ring': [stalk_color_below_ring],
        'veil_type': [veil_type],
        'veil_color': [veil_color],
        'ring_number': [ring_number],
        'ring_type': [ring_type],
        'spore_print_color': [spore_print_color],
        'population': [population],
        'habitat': [habitat]
    })

    # Make a prediction using the classification model
    prediction = predict_model(classification_model, data=input_data)
    predicted_class = prediction['Label'][0]

    # Return the result to the template
    return render_template('jess_index.html', prediction=predicted_class)

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port, debug=True)
 
