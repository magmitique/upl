class BadRange(Exception):
    """Exception raised when provided value is not in defined range."""

    def __init__(self, message="Not in defined range"):
        self.message = message
        super().__init__(self.message)

class InvalidException(Exception):
    """Exception raised when custom exception asked is invalid."""

    def __init__(self, message="Invalid Exception"):
        self.message = message
        super().__init__(self.message)

def doraise(error, message=None):
    if error=="BadRange":
        err = BadRange(message=message if message else None)
    else:
        raise InvalidException
    raise err