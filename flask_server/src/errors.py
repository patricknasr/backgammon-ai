class InvalidMove(Exception):
    """Exception raised for player attempting to move a piece where two or more opponent pieces exist.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Cannot move piece here"):
        self.message = message
        super().__init__(self.message)

class InvalidColour(Exception):
    """Exception raised for player attempting to move a piece of undefined colour.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Colour does not exist."):
        self.message = message
        super().__init__(self.message)