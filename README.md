
# Flask Application with Hugging Face Model and Unit Tests

This repository contains a Flask application that uses a Hugging Face model for sequence classification. The application provides a `/predict` endpoint to perform predictions based on input text. Additionally, unit tests are included to ensure the functionality of the application.

## Files

- `app.py`: Contains the Flask application code.
- `test_app.py`: Contains the unit tests for the Flask application.

## Requirements

- Python 3.7+
- Flask
- TensorFlow
- tf-keras
- transformers (Hugging Face library)
- unittest (Python standard library)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/gregorymarchal/projet_7-api.git
   cd projet_7-api
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

   There is a `requirements.txt` file, but you can also install the dependencies manually:

   ```sh
   pip install flask tensorflow transformers
   ```

## Running the Application

To run the Flask application locally, use the following command:

```sh
python app.py
```

By default, the application will be accessible at `http://127.0.0.1:5000`.

## Using the `/predict` Endpoint

The `/predict` endpoint accepts POST requests with a JSON payload containing the text to be classified. Example:

```sh
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"text": "This is a test sentence."}'
```

The response will be a JSON array containing the predicted class.

## Running the Unit Tests

To run the unit tests, use the following command:

```sh
python -m unittest test_app.py
```

The tests will check the `/predict` endpoint to ensure it returns the correct status code, content type, and response structure.

## Deployment on Azure

When deploying to Azure WebApp, ensure that the `app.py` file is set up correctly. Azure WebApp will use the `app` instance to run the application.
