# Import required libraries and functions
import unittest
from acme import Product
from acme_report import generate_products, adj, nns

# Create test class
class AcmeProductTests(unittest.TestCase):
    def test_default_product_price(self):
        # Test default product price being 10.
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    # Create additional method 1
    def test_default_values(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10, msg='The default price is not matching.')
        self.assertEqual(prod.weight, 20, msg='The default weight is not matching.')
        self.assertEqual(prod.flammability, 0.5, msg='The default flammability is not matching.')


if __name__ == '__main__':
    unittest.main()
