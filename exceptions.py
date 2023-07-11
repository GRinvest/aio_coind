

class CoindError(Exception):
    """
    Exception class for Coind errors.

    Attributes:
        code (int): Error code.
        msg (str): Error message.
    """

    def __init__(self, error_code, error_message):
        """
        Initialize the CoindError instance.

        Args:
            error_code (int): Error code.
            error_message (str): Error message.
        """
        self.code = error_code
        self.msg = error_message
