import os
import unittest
from dotenv import load_dotenv
from .lomadee import Offers

def load_env():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv(os.path.join(BASE_DIR, '.env'))

class TestOffers(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        load_env()
        self.offers =  Offers(
            os.environ.get('APP_TOKEN'),
            os.environ.get('SOURCE_ID'),
            sandbox=True,
            version='v3'
        )
   
    def test_category(self):
        response = self.offers.category(
            '77', page=1, size=10
        )
        
        self.assertEqual(response['requestInfo']['status'], 'OK')
        self.assertEqual(response['requestInfo']['message'], 'SUCCESS')
        self.assertEqual(response['pagination']['page'], 1)
        self.assertEqual(response['pagination']['size'], 10)

    def test_store(self):
        response = self.offers.store(
            '5766', page=1, size=10
        )

        self.assertEqual(response['requestInfo']['status'], 'OK')
        self.assertEqual(response['requestInfo']['message'], 'SUCCESS')
        self.assertEqual(response['pagination']['page'], 1)
        self.assertEqual(response['pagination']['size'], 10)

if __name__ == '__main__':
    unittest.main()