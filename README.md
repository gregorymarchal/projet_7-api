# Flask TensorFlow Prediction API

This project is a Flask application that uses a pre-trained TensorFlow model for sequence classification and provides endpoints for predictions and feedback.

## Setup

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)

### Install Dependencies

1. Clone the repository:
    ```sh
    git clone https://github.com/gregorymarchal/projet_7-api.git
    cd projet_7-api
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. Set up the Azure Application Insights connection string in your environment:
    ```sh
    CONNECTION_STRING="<your_connection_string>"
    ```

2. Run the Flask application:
    ```sh
    gunicorn app:app
    ```

The application will be available at `http://localhost:8000`.

### Endpoints

#### POST /predict

This endpoint accepts a JSON payload with a `text` field and returns the prediction result.

- **Request:**
    ```json
    {
        "text": "Sample text for prediction"
    }
    ```

- **Response:**
    ```json
    [0] (if negative prediction)
    [1] (if positive prediction)
    ```

#### POST /feedback

This endpoint accepts user feedback and logs it to Azure Application Insights.

- **Request:**
    ```json
    {
        "text_input": "Sample text for prediction",
        "predicted_sentiment": "negatif OU positif"
        "feedback": "Non"
    }
    ```

- **Response:**
    ```json
    {
        "message": "Feedback received successfully."
    }
    ```

### Running Tests

To run the unit tests, use the following command:
```sh
python3 -m unittest test_app.py
