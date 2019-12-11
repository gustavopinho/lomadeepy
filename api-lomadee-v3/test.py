import os
import unittest
from dotenv import load_dotenv
from .lomadee import Offers, Categories, Stores, Coupons, DeepLink

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

    def test_offer(self):
        response = self.offers.offer(
            '5632','1218071477'
        )
        self.assertEqual(response['requestInfo']['status'], 'OK')
        self.assertEqual(response['requestInfo']['message'], 'SUCCESS')
        self.assertEqual(response['pagination']['page'], 1)
        self.assertEqual(response['pagination']['size'], 1)

    def test_search(self):
        response = self.offers.search(
            'Samsung', page=1, size=10
        )
        self.assertEqual(response['requestInfo']['status'], 'OK')
        self.assertEqual(response['requestInfo']['message'], 'SUCCESS')
        self.assertEqual(response['pagination']['page'], 1)
        self.assertEqual(response['pagination']['size'], 10)


class TestCategories(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        load_env()
        self.categories =  Categories(
            os.environ.get('APP_TOKEN'),
            os.environ.get('SOURCE_ID'),
            sandbox=True,
            version='v3'
        )

    def test_all(self):
        response = self.categories.all()
        self.assertEqual(response['requestInfo']['status'], 'OK')
        self.assertEqual(response['requestInfo']['message'], 'SUCCESS')

    def test_category(self):
        response = self.categories.category('77')
        self.assertEqual(response['requestInfo']['status'], 'OK')
        self.assertEqual(response['requestInfo']['message'], 'SUCCESS')
        self.assertEqual(response['pagination']['page'], 1)
        self.assertEqual(response['pagination']['size'], 1)

    def test_search(self):
        response = self.categories.search('Celular e Smartphone')
        self.assertEqual(response['requestInfo']['status'], 'OK')
        self.assertEqual(response['requestInfo']['message'], 'SUCCESS')


class TestStores(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        load_env()
        self.stores =  Stores(
            os.environ.get('APP_TOKEN'),
            os.environ.get('SOURCE_ID'),
            sandbox=True,
            version='v3'
        )

    def test_all(self):
        response = self.stores.all()
        self.assertEqual(response['requestInfo']['status'], 'OK')
        self.assertEqual(response['requestInfo']['message'], 'SUCCESS')


class TestCoupons(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        load_env()
        self.coupons =  Coupons(
            os.environ.get('APP_TOKEN'),
            os.environ.get('SOURCE_ID'),
            sandbox=True,
            version='v2'
        )

    def test_all(self):
        response = self.coupons.all()
        self.assertEqual(response['requestInfo']['status'], 'OK')
        self.assertEqual(response['requestInfo']['message'], 'SUCCESS')

    def test_coupon(self):
        response = self.coupons.coupon('8165')
        self.assertEqual(response['requestInfo']['status'], 'OK')
        self.assertEqual(response['requestInfo']['message'], 'SUCCESS')

    def test_category(self):
        response = self.coupons.categories()
        self.assertEqual(response['requestInfo']['status'], 'OK')
        self.assertEqual(response['requestInfo']['message'], 'SUCCESS')

    def test_store(self):
        response = self.coupons.stores()
        self.assertEqual(response['requestInfo']['status'], 'OK')
        self.assertEqual(response['requestInfo']['message'], 'SUCCESS')


class TestDeepLink(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        load_env()
        self.deepLink =  DeepLink(
            os.environ.get('APP_TOKEN'),
            os.environ.get('SOURCE_ID'),
            sandbox=True,
            version='v2'
        )

    def test_create(self):
        response = self.deepLink.create('https://www.americanas.com.br/')
        self.assertEqual(response['requestInfo']['status'], 'OK')
        self.assertEqual(response['requestInfo']['message'], 'SUCCESS')


if __name__ == '__main__':
    unittest.main()