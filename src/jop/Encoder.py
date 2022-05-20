import re
from jop.JsonNode import JsonNode, KVPair
from jop.JsonCase import JsonCase
from jop.Maybe import Maybe, Error, Just


class Encoder:
    """
    Encoding input into a variety of output formats

    All IO should be contained in __main__.py!!
    """

    DELINIATOR = "="

    def __init__(self) -> None:
        self.x = 10

    @staticmethod    
    def _eval_case(args: str) -> JsonCase:

        # if key=val, then case 0
        pass
        # unless key=$(), then we have a nested case


    @staticmethod
    def to_json(args: list) -> str:
        root_node = JsonNode()

        for arg in args:
            # case 1: k=v            

            # split the pair
            key, val = Encoder._key_value_split(arg)

            # keys must be enclosed in quotes
            key = Encoder._add_double_quote(key)

            # if the val is not an integer, float, or bool then it must be quotified
            if Encoder._is_string(val, switch=False) and not Encoder._is_double_quoted(
                val
            ):
                val = Encoder._add_double_quote(val)

            kvpair = KVPair(key, val)
            root_node.add_data(kvpair)


        return str(root_node)

    @staticmethod
    def node_builder(node: JsonNode, args: list) -> JsonNode:
        if args == []:
            return node

        grouping_operator = '#'

        # pop the arg
        arg = args.pop(0)

        # case 0 k=v
        if '=' in arg and grouping_operator not in arg:
            key, val = Encoder._key_value_split(arg)
            key = Encoder._add_double_quote(key)
            if Encoder._is_string(val, switch=False) and not Encoder._is_double_quoted(
                val
            ):
                val = Encoder._add_double_quote(val)

            node.add_data(KVPair(key, val))
            return Encoder.node_builder(node, args)

        # catch all, we had an error
        return None
        

    @staticmethod
    def _update_json_node(node: JsonNode, arg) -> JsonNode:
        # eval an arg and update a json node as needed

        grouping_operator = '#'

        # case 0 k=v
        if '=' in arg and grouping_operator not in arg:
            key, val = Encoder._key_value_split(arg)
            node.add_data(KVPair(key, val))
            return node

        # case 1 k=-k=v-
        if grouping_operator in arg:
            key, nested_object = Encoder._key_value_split(arg)
            node.add_data(KVPair(key, 'nested object here!'))
            return node

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
        # str -> bool -> bool
        # return true if:
        # is not only integers (0-9)
        # is not a float
        # is not a bool (t, f, True, False)

        # Maybe Example:
        # getting values
        # if type(input) == Error:
        #     return Error(error_message=f'error in example function :->: {input.error_message}')
        # if type(switch) == Error:
        #     return Error(error_message=f'error in example function :->: {input.error_message}')
        # input = input.val
        # switch = switch.val


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

    @staticmethod
    def _example_function(val: Maybe) -> Maybe:
        """
        example of using the Maybe type
        """

        # pattern match
        if type(val) == Error:
            return Error(error_message=f'error in example function :->: {val.error_message}')

        if type(val) == Just:
            val = val.val

            # do some stuff with val            

            return Just(val)
