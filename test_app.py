import unittest
import json
from flask import Flask
from flask.testing import FlaskClient
from unittest.mock import patch, MagicMock

# Import the app from your script
from app import app, model, tokenizer, logger

class FlaskAppTestCase(unittest.TestCase):import unittest
import json
from flask import Flask
from flask.testing import FlaskClient
from unittest.mock import patch, MagicMock

# Import the app from your script
from app import app, model, tokenizer, logger

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch("app.tokenizer")
    @patch("app.model")
    def test_predict(self, mock_model, mock_tokenizer):
        # Mocking the tokenizer output
        mock_tokenizer.return_value = {"input_ids": [[1, 2, 3]], "attention_mask": [[1, 1, 1]]}

        # Mocking the model output
        mock_model.return_value = MagicMock(logits=[[0.1, 0.9]])

        response = self.app.post("/predict", 
                                 data=json.dumps({"text": "Test input"}),
                                 content_type="application/json")
        
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check if the response data is as expected
        response_data = json.loads(response.data)
        self.assertEqual(response_data, [1])

    @patch("app.logger")
    def test_feedback(self, mock_logger):
        feedback_data = {"text": "Great model!"}
        
        response = self.app.post("/feedback",
                                 data=json.dumps(feedback_data),
                                 content_type="application/json")

        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check if the response data is as expected
        response_data = json.loads(response.data)
        self.assertEqual(response_data, {"message": "Feedback received successfully."})
        
        # Check if the logger was called with the correct feedback
        mock_logger.warning.assert_called_with(f"User feedback: {feedback_data}")

if __name__ == "__main__":
    unittest.main()

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.tokenizer')
    @patch('app.model')
    def test_predict(self, mock_model, mock_tokenizer):
        # Mocking the tokenizer output
        mock_tokenizer.return_value = {'input_ids': [[1, 2, 3]], 'attention_mask': [[1, 1, 1]]}

        # Mocking the model output
        mock_model.return_value = MagicMock(logits=[[0.1, 0.9]])

        response = self.app.post('/predict', 
                                 data=json.dumps({'text': 'Test input'}),
                                 content_type='application/json')
        
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check if the response data is as expected
        response_data = json.loads(response.data)
        self.assertEqual(response_data, [1])

    @patch('app.logger')
    def test_feedback(self, mock_logger):
        feedback_data = {'text': 'Great model!'}
        
        response = self.app.post('/feedback',
                                 data=json.dumps(feedback_data),
                                 content_type='application/json')

        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check if the response data is as expected
        response_data = json.loads(response.data)
        self.assertEqual(response_data, {"message": "Feedback received successfully."})
        
        # Check if the logger was called with the correct feedback
        mock_logger.warning.assert_called_with(f"User feedback: {feedback_data}")

if __name__ == '__main__':
    unittest.main()
