# Import necessary modules from Flask and TensorFlow, and Hugging Face's Transformers library
import os
from flask import Flask, request, jsonify
import tensorflow as tf
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

# Create a Flask application instance
app = Flask(__name__)

# Define the model name from Hugging Face Hub
model_name = "gregorymarchal/projet-7-trained-distilbert"

# Load the pre-trained model for sequence classification
model = TFAutoModelForSequenceClassification.from_pretrained(model_name)

# Load the corresponding tokenizer for the model
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Set up logging to Azure Application Insights
connection_string = os.getenv('CONNECTION_STRING')
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string=connection_string))

# Define a route for prediction, accepting POST requests
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.json
    
    # Tokenize the input text and convert it to tensor format
    inputs = tokenizer(data['text'], return_tensors='tf')
    
    # Perform the prediction using the model
    outputs = model(inputs)
    
    # Get the predicted class by finding the index of the highest logit
    predictions = tf.argmax(outputs.logits, axis=-1).numpy().tolist()
    
    # Return the predictions as a JSON response
    return jsonify(predictions)

# Define a route for feedback, accepting POST requests
@app.route('/feedback', methods=['POST'])
def feedback():
    # Get the JSON data from the request
    feedback_data = request.json
    
    # Log the feedback data to Azure Application Insights
    logger.warning(f"User feedback: {feedback_data}")
    
    # Return a success message
    return jsonify({"message": "Feedback received successfully."}), 200
