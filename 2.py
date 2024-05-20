import unittest
from coinbaseloader import CoinBaseLoader

class TestCoinBaseLoader(unittest.TestCase):
    def setUp(self):
        self.loader = CoinBaseLoader()

    def test_load_data(self):
        data = self.loader.load_data()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    @unittest.expectedFailure
    def test_invalid_symbol(self):
        with self.assertRaises(ValueError):
            self.loader.load_symbol('INVALID_SYMBOL')

    @unittest.skip("Потребує доступу до Інтернету")
    def test_load_symbol(self):
        symbol_data = self.loader.load_symbol('BTC-USD')
        self.assertIsNotNone(symbol_data)
        self.assertIsInstance(symbol_data, dict)
        self.assertIn('symbol', symbol_data)
        self.assertEqual(symbol_data['symbol'], 'BTC-USD')

if __name__ == '__main__':
    unittest.main()
