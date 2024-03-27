"""
Enigma plugboard class

Olivier Boesch - 2024
"""


class Plugboard:
    """
    Enigma plug board object
    """
    def __init__(self, letter_couples: list[str] | None = None) -> None:
        """
        Create the plug board object
        :param letter_couples: list of str of exchanging letters
        """
        self.exchange_dict: dict = {}
        if letter_couples is not None:
            for couple in letter_couples:
                l1 = couple[0]
                l2 = couple[1]
                self.exchange_dict[l1] = l2
                self.exchange_dict[l2] = l1
        self.next: "Rotor" = None

    def __str__(self) -> str:
        """
        String representation of the plug board config
        :return:
        """
        return f"Plugboard: {self.exchange_dict}"

    def encode_forward(self, letter:str) -> str | None:
        """
        Encode forward letter with plugboard if applicable and pass to the next object
        otherwise just pass to next object end returns the result
        return letter if there's no next object (for tests)
        :param letter:
        :return: return encoded letter
        """
        if letter in self.exchange_dict:
            letter = self.exchange_dict[letter]
        if self.next is not None:
            return self.next.encode_forward(letter)
        else:
            return letter

    def encode_backward(self, letter:str) -> str | None:
        """
        Encode forward letter with plugboard if applicable and return the encoded letter
        otherwise just return the encoded letter
        :param letter: letter to encode
        :return: encoded letter
        """
        if letter in self.exchange_dict:
            letter = self.exchange_dict[letter]
        return letter

    def rotate(self) -> None:
        """
        Calls rotate for the next object (a rotor)
        :return: None
        """
        if self.next is not None:
            self.next.rotate()
