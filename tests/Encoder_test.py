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

class to_array_test(unittest.TestCase):
    # 1 element
    def test_1_elem(self):
        data = ['1']
        expected_result = '[1]'

        result = Encoder.to_array(data)

        self.assertEqual(
            result,
            expected_result
        )

    # 2 elements
    def test_2_elem(self):
        data = ['1', '2']
        expected_result = '[1, 2]'

        result = Encoder.to_array(data)

        self.assertEqual(
            result,
            expected_result
        )

    def test_0_elem(self):
        data = []
        expected_result = '[]'

        result = Encoder.to_array(data)

        self.assertEqual(
            result,
            expected_result
        )

    def test_1_string(self):
        data = ['value']
        expected_result = '[value]'

        result = Encoder.to_array(data)

        self.assertEqual(
            result,
            expected_result
        )

    def test_2_string(self):
        data = ['value', 'another value']
        expected_result = '[value, another value]'

        result = Encoder.to_array(data)

        self.assertEqual(
            result,
            expected_result
        )

    def test_mixed_types(self):
        # but not really
        data = ['value', '1']
        expected_result = '[value, 1]'

        result = Encoder.to_array(data)

        self.assertEqual(
            result,
            expected_result
        )

    def test_repeated_elements(self):
        data = ['value', 'value']
        expected_result = '[value, value]'

        result = Encoder.to_array(data)

        self.assertEqual(
            result,
            expected_result
        )


if __name__ == '__main__':
    unittest.main()