from flask import Flask, request, jsonify
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer

app = Flask(__name__)

# Load model and tokenizer from Hugging Face Hub
model_name = "gregorymarchal/projet-7-trained-distilbert"
model = TFAutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    inputs = tokenizer(data['text'], return_tensors='tf')
    outputs = model(inputs)
    predictions = tf.argmax(outputs.logits, axis=-1).numpy().tolist()
    return jsonify(predictions)
