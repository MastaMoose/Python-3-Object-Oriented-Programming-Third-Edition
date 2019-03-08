class SecretString:
    """A not-at-all secure way to store a secret string."""

    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        """Only show the string if the pass_phrase is correct."""
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ""

class NotSecretString:
    """A not-at-all secure way to store a secret string."""

    def __init__(self, plain_string, pass_phrase):
        self._plain_string = plain_string
        self._pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        """Only show the string if the pass_phrase is correct."""
        if pass_phrase == self._pass_phrase:
            return self._plain_string
        else:
            return ""
        
class PublicString:
    """A not-at-all secure way to store a secret string."""

    def __init__(self, plain_string, pass_phrase):
        self.plain_string = plain_string
        self.pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        """Only show the string if the pass_phrase is correct."""
        if pass_phrase == self.pass_phrase:
            return self.plain_string
        else:
            return ""