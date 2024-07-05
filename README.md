# Text Classification API

This repository contains a simple Flask API for text classification using a pre-trained DistilBERT model from Hugging Face. The API accepts text input via a POST request and returns the predicted class.

## Setup

### Prerequisites

- Python 3.7+
- Flask
- TensorFlow
- Transformers (Hugging Face)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/gregorymarchal/projet_7-api.git
    cd projet_7-api
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install flask tensorflow transformers
    ```

## Usage

### Running the API

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. The server will start on `http://127.0.0.1:5000`.

### Making Predictions

Send a POST request to `http://127.0.0.1:5000/predict` with a JSON payload containing the text you want to classify.

Example:
```bash
curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" -d '{"text": "Your text here"}'
