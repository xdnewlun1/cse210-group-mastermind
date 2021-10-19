class Code:
    """The secret code to be guessed in the game. The responsibility of Code is to generate the new code and do guess checking against player guesses.

    Stereotype:
        Service Provider, Information Holder

    Attributes:
        _code (int): The Games Secret Code
    """

    def __init__(self):
        """The class constructor.

        """
        self._code = format(random.randint(1000,9999), '04d')