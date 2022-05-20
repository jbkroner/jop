class Maybe:
    def __init__(self) -> None:
        return

class Error(Maybe):
    def __init__(self, error_message) -> None:
        super().__init__()
        self.error_message = error_message

class Just(Maybe):
    def __init__(self, val) -> None:
        super().__init__()
        self.val = val


