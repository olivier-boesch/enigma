"""
Enigma reflector class and configs

Olivier Boesch - 2024
"""
import string

"""
REFLECTOR : Enigma reflector configs
"""
REFLECTORS = {
    "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
    # Wehrmacht and Luftwaffe
    "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
    "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
    #  Kriegsmarine M4 only
    "B-thin": "ENKQAUYWJICOPBLMDXZVFTHRGS",
    "C-thin": "RDOBJNTKVEHMLFCWZAXGYIPSUQ"
}


class Reflector:
    """
    Enigma machine Reflector Class
    """
    def __init__(self, name: str = "") -> None:
        """
        Create a relfector by its model name
        :param name: model of the reflector
        """
        # stores the name
        self.name = name
        # if the name is not known
        if name not in REFLECTORS:
            raise Exception("Invalid Reflector name")
        # stores the sequence
        self.sequence: str = REFLECTORS[name]
        # create previous and next (next is always None as there's notthing after the reflector)
        self.previous = None
        self.next = None

    def __str__(self) -> str:
        """
        Return a string representation of the reflector config
        :return:
        """
        return f"Reflector: {self.name}, sequence: {self.sequence}"

    def encode_forward(self, letter: str):
        """
        Encode a letter with the reflector and go backward to the previous rotor
        :param letter: letter to encode
        :return: the encoded letter if there's no previous object(for tests) or the results of the previous rotor encoding
        """
        letter_index = string.ascii_uppercase.index(letter)
        letter_encoded = self.sequence[letter_index]
        if self.previous is not None:
            return self.previous.encode_backward(letter_encoded)
        else:
            return letter_encoded

    def rotate(self):
        """
        Does nothing (a reflector is not a moving part)
        exists to stop next.rotate call chain
        """
        pass


# tests
if __name__ == "__main__":
    reflector = Reflector(name="B")
    assert reflector.encode_forward("B") == "R"
    assert reflector.encode_forward("Y") == "A"
