import unittest
import json
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict(self):
        response = self.app.post('/predict', 
                                 data=json.dumps({'text': 'Hello world!'}), 
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)

    def test_feedback(self):
        feedback_data = {
            "user_id": "12345",
            "feedback": "This is a feedback message."
        }
        response = self.app.post('/feedback', 
                                 data=json.dumps(feedback_data), 
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['message'], "Feedback received successfully.")

if __name__ == '__main__':
    unittest.main()
