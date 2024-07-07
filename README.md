# Flask TensorFlow Prediction API

This project is a Flask application that uses a pre-trained TensorFlow model for sequence classification and provides endpoints for predictions and feedback.

## Setup

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)

### Install Dependencies

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. Set up the Azure Application Insights connection string in `app.py`:
    ```python
    connection_string = "InstrumentationKey=your_instrumentation_key;IngestionEndpoint=your_ingestion_endpoint"
    ```

2. Run the Flask application:
    ```sh
    python app.py
    ```

The application will be available at `http://127.0.0.1:5000`.

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
    [0]
    ```

#### POST /feedback

This endpoint accepts user feedback and logs it to Azure Application Insights.

- **Request:**
    ```json
    {
        "user_id": "12345",
        "feedback": "This is a feedback message."
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
python -m unittest test_app.py
