class Encoder:
    """
    Encoding input into a variety of output formats

    All IO should be contained in __main__.py!!
    """
    DELINIATOR = '='

    def __init__(self) -> None:
        self.x = 10

    @staticmethod
    def to_json(args: str) -> str:
        encoded_data = "{\n\t"
        for arg in args:
            key, val = Encoder._key_value_split(arg)
            encoded_data = encoded_data + f'{key} : {val}' + "\n\t"

        encoded_data = encoded_data + "\n}"
        return encoded_data 

    @staticmethod
    def _key_value_split(key_value_pair: str) -> str:
        if Encoder.DELINIATOR in key_value_pair:
            kv_list= key_value_pair.split(Encoder.DELINIATOR)
            return kv_list[0], kv_list[1]

    