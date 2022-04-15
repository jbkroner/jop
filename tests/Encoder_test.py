import unittest
from src.jop.Encoder import Encoder

class key_value_split_test(unittest.TestCase):
    def test_000(self):
        key='key'
        val='val'
        kvp = key + '=' + val
        result_key, result_val = Encoder._key_value_split(kvp)

        self.assertEqual(
            key,
            result_key
        )

        self.assertEqual(
            val,
            result_val
        )

if __name__ == '__main__':
    unittest.main()