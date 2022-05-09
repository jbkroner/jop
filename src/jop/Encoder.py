import re
from typing import Tuple

from JsonNode import JsonNode


class Encoder:
    """
    Encoding input into a variety of output formats

    All IO should be contained in __main__.py!!
    """

    DELINIATOR = "="

    def __init__(self) -> None:
        self.x = 10

    @staticmethod
    def to_json(args: list) -> str:
        encoded_data = []
        for arg in args:
            key, val = Encoder._key_value_split(arg)

            # keys must be enclosed in quotes
            key = Encoder._add_double_quote(key)

            # TODO fix this

            # if the val is not an integer, float, or bool then it must be quotified
            # TODO - add switch mode support to to_json
            # TODO - type coercion on bools
            # TODO - nested objects
            if Encoder._is_string(val, switch=False) and not Encoder._is_double_quoted(
                val
            ):
                val = Encoder._add_double_quote(val)

            node = JsonNode(key=key, val=val)

            print(node.key)

            encoded_data.append(node)

        return Encoder._stringify_encoded_data(encoded_data=encoded_data, pretty=False)

    @staticmethod
    def _stringify_encoded_data(encoded_data: list[JsonNode], pretty: bool) -> str:
        if not pretty:
            output = "{"
            for kvpair in encoded_data:
                if kvpair != encoded_data[0]:
                    output = output + ', '  + str(kvpair)
                else:
                    output = output + str(kvpair)
            output = output + '}'
            return output


    @staticmethod
    def to_array(args: list) -> str:
        # TODO pass in quotes? maybe fix through type coercion. original implementation does not deal with this at all.
        encoded_data = "["
        for index, arg in enumerate(args):
            if arg[0] == '"' and arg[0] == '"':
                arg = Encoder._add_double_quote(arg)
            encoded_data = encoded_data + str(arg)
            if index != len(args) - 1:
                encoded_data = encoded_data + ", "

        encoded_data = encoded_data + "]"

        return encoded_data

    @staticmethod
    def _key_value_split(key_value_pair: str) -> str:
        if Encoder.DELINIATOR in key_value_pair:
            kv_list = key_value_pair.split(Encoder.DELINIATOR)
            return kv_list[0], kv_list[1]

    @staticmethod
    def _add_double_quote(input: str) -> str:
        # quotify a string

        escaped_double_quote = '"'

        if input[0] != escaped_double_quote:
            input = escaped_double_quote + input

        if input[1] != escaped_double_quote:
            input = input + escaped_double_quote

        return input

    @staticmethod
    def _is_double_quoted(input: str) -> bool:
        if len(input) > 2:
            return input[0] == '"' and input[-1] == '"'
        return False

    @staticmethod
    def _is_string(input: str, switch: bool) -> bool:
        # return true if:
        # is not only integers (0-9)
        # is not a float
        # is not a bool (t, f, True, False)
        has_digits = input.isdigit()
        has_bool = False

        # check if it's a float
        # https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python
        if not re.match(r"^-?\d+(?:\.\d+)$", input) is None:
            has_digits = True

        # check for bools / null if not in switch mode
        if not switch:
            if input in ["true", "false", "null"]:
                has_bool = True

        if has_digits or has_bool:
            return False
        return True
