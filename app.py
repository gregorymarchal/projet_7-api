# Import necessary modules from Flask and TensorFlow, and Hugging Face's Transformers library
from flask import Flask, request, jsonify
import tensorflow as tf
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer

# Create a Flask application instance
app = Flask(__name__)

# Define the model name from Hugging Face Hub
model_name = "gregorymarchal/projet-7-trained-distilbert"

# Load the pre-trained model for sequence classification
model = TFAutoModelForSequenceClassification.from_pretrained(model_name)

# Load the corresponding tokenizer for the model
tokenizer = AutoTokenizer.from_pretrained(model_name)

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

# If this script is run directly, start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
