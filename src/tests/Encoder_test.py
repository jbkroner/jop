import unittest
from src.jop.Encoder import Encoder


class key_value_split_test(unittest.TestCase):
    def test_000(self):
        key = "key"
        val = "val"
        kvp = key + "=" + val
        result_key, result_val = Encoder._key_value_split(kvp)

        self.assertEqual(key, result_key)

        self.assertEqual(val, result_val)


class to_array_test(unittest.TestCase):
    # 1 element
    def test_1_elem(self):
        data = ["1"]
        expected_result = "[1]"

        result = Encoder.to_array(data)

        self.assertEqual(result, expected_result)

    # 2 elements
    def test_2_elem(self):
        data = ["1", "2"]
        expected_result = "[1, 2]"

        result = Encoder.to_array(data)

        self.assertEqual(result, expected_result)

    def test_0_elem(self):
        data = []
        expected_result = "[]"

        result = Encoder.to_array(data)

        self.assertEqual(result, expected_result)

    def test_1_string(self):
        data = ["value"]
        expected_result = "[value]"

        result = Encoder.to_array(data)

        self.assertEqual(result, expected_result)

    def test_2_string(self):
        data = ["value", "another value"]
        expected_result = "[value, another value]"

        result = Encoder.to_array(data)

        self.assertEqual(result, expected_result)

    def test_mixed_types(self):
        # but not really
        data = ["value", "1"]
        expected_result = "[value, 1]"

        result = Encoder.to_array(data)

        self.assertEqual(result, expected_result)

    def test_repeated_elements(self):
        data = ["value", "value"]
        expected_result = "[value, value]"

        result = Encoder.to_array(data)

        self.assertEqual(result, expected_result)


class add_double_quote_test(unittest.TestCase):
    CASES = [
        ["test", '"test"'],
        ["they're", '"they\'re"'],
        ["they're", '"they\'re"'],
        ["they are", '"they are"'],
    ]

    def test_all_cases(self):
        for case in self.CASES:
            self.assertEqual(Encoder._add_double_quote(case[0]), case[1])


class is_double_quoted_test(unittest.TestCase):
    CASES = [
        ["", False],
        [" ", False],
        ["  ", False],
        ['"', False],
        ['""', False],
        ["abc", False],
        ['"abc"', True],
    ]

    def test_all_cases(self):
        for case in self.CASES:
            self.assertEqual(Encoder._is_double_quoted(case[0]), case[1])


class _is_string(unittest.TestCase):
    SWITCH_MODE_FALSE_CASES = [
        ["1", False],
        # ['1.0', False],
        # ['true', False],
        # ['false', False],
        # ['test', True],
        # ['test', True],
        # ['testTrue', True],
        # ['test1234', True],
        # ['test1234.1234', True],
    ]

    def test_switch_mode_false_000(self):
        input = "1"
        expected = False
        self.assertEqual(Encoder._is_string(input, switch=False), expected)

    def test_switch_mode_false_001(self):
        input = "1.0"
        expected = False
        self.assertEqual(Encoder._is_string(input, switch=False), expected)

    def test_switch_mode_false_002(self):
        input = "true"
        expected = False
        self.assertEqual(Encoder._is_string(input, switch=False), expected)

    def test_switch_mode_false_003(self):
        input = "false"
        expected = False
        self.assertEqual(Encoder._is_string(input, switch=False), expected)

    def test_switch_mode_false_004(self):
        input = "null"
        expected = False
        self.assertEqual(Encoder._is_string(input, switch=False), expected)

    def test_switch_mode_false_005(self):
        input = "a"
        expected = True
        self.assertEqual(Encoder._is_string(input, switch=False), expected)

    def test_switch_mode_false_006(self):
        input = "a1"
        expected = True
        self.assertEqual(Encoder._is_string(input, switch=False), expected)

    def test_switch_mode_false_007(self):
        input = "atrue"
        expected = True
        self.assertEqual(Encoder._is_string(input, switch=False), expected)

    def test_switch_mode_true_000(self):
        input = "1"
        expected = False
        self.assertEqual(Encoder._is_string(input, switch=True), expected)

    def test_switch_mode_true_001(self):
        input = "1.0"
        expected = False
        self.assertEqual(Encoder._is_string(input, switch=True), expected)

    def test_switch_mode_true_002(self):
        input = "true"
        expected = True
        self.assertEqual(Encoder._is_string(input, switch=True), expected)

    def test_switch_mode_true_003(self):
        input = "false"
        expected = True
        self.assertEqual(Encoder._is_string(input, switch=True), expected)

    def test_switch_mode_true_004(self):
        input = "null"
        expected = True
        self.assertEqual(Encoder._is_string(input, switch=True), expected)

    def test_switch_mode_true_005(self):
        input = "a"
        expected = True
        self.assertEqual(Encoder._is_string(input, switch=True), expected)

    def test_switch_mode_true_006(self):
        input = "a1"
        expected = True
        self.assertEqual(Encoder._is_string(input, switch=True), expected)

    def test_switch_mode_true_007(self):
        input = "atrue"
        expected = True
        self.assertEqual(Encoder._is_string(input, switch=True), expected)


if __name__ == "__main__":
    unittest.main()
