import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client for the Flask application
        self.app = app.test_client()
        self.app.testing = True

    def test_predict(self):
        # Define a test case for the predict route
        response = self.app.post('/predict', json={'text': 'This is a test sentence.'})
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the response is a JSON object
        self.assertEqual(response.content_type, 'application/json')
        
        # Check if the response contains a list of predictions
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)  # Assuming the model outputs one prediction

if __name__ == '__main__':
    unittest.main()
