"""
Enigma rotor class and configs

Olivier Boesch - 2024
"""
import string

"""
ROTORS : Enigma rotors config and notches
"""
ROTORS = {
    # "name": ("sequence", "notches")
    # Enigma (Wehrmacht and Kriegsmarine)
    "I": ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    "II": ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    "III": ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    "IV": ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    "V": ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
    # Kriegsmarine M3 and M4 only
    "VI": ("JPGVOUMFYQBENHZRDKASXLICTW", "ZM"),
    "VII": ("NZJHGRCXMYSWBOUFAIVLPEKQDT", "ZM"),
    "VIII": ("FKQHTLXOCBJSPDZRAMEWNIUYGV", "ZM")
}


class Rotor:
    """
    Enigma machine Rotor Class
    """
    def __init__(self, name: str = "", start_letter: str = "A") -> None:
        """
        Create a new rotor of the given name and sets it to its start position
        :param name: model of the rotor
        :param start_letter: starting letter
        """
        # create next and previous
        self.next: "Rotor" = None
        self.previous: "Rotor" = None
        # stores the name and starting position (0 for A, 1 for B, ...)
        self.name = name
        self.rotor_pos = 0
        # check if the rotor is known
        if name not in ROTORS.keys():  # unknown rotor
            raise Exception("Invalid Rotor Name")
        # stores sequence
        self.sequence: str = ROTORS[name][0]
        # stores notches
        self.notches: str = ROTORS[name][1]
        # go in start position
        self.go_to_start(start_letter)

    def __str__(self):
        """
        Return a string representation of the rotor config and current state
        :return:
        """
        return f"Rotor: {self.name}, actual sequence: {self.sequence}, current pos: {string.ascii_uppercase[self.rotor_pos]}"

    def go_to_start(self, letter):
        """
        Move the rotor to the start letter and update the current position
        doesn't rotate the next rotors
        :param letter:
        :return:
        """
        remaining_steps = string.ascii_uppercase.index(letter.upper())
        self.rotor_pos = remaining_steps
        while remaining_steps > 0:
            self.sequence = self.sequence[1:] + self.sequence[0]
            remaining_steps -= 1

    def encode_forward(self, letter):
        """
        Encodes a letter forward and pass to the next object
        return encoded letter if there's no next object (for tests)
        :param letter: letter to encode
        :return: return the result of the encoded letter
        """
        letter_index = string.ascii_uppercase.index(letter)
        encoded_letter = self.sequence[letter_index]
        if self.next is not None:
            return self.next.encode_forward(encoded_letter)
        else:
            return encoded_letter

    def encode_backward(self, letter):
        """
        Encodes a letter backward and pass to the previous object
        return encoded letter if there's no previous object (for tests)
        :param letter: letter to encode
        :return: return the result of the encoded letter
        """
        letter_index = self.sequence.index(letter)
        encoded_letter = string.ascii_uppercase[letter_index]
        if self.previous is not None:
            return self.previous.encode_backward(encoded_letter)
        else:
            return encoded_letter

    def rotate(self):
        """
        Rotates the rotor and call rotate for the next object if a notch was passed
        """
        self.sequence = self.sequence[1:] + self.sequence[0]
        self.rotor_pos = (self.rotor_pos + 1) % 26
        # a notch is passed - > rotate the next one (on the left)
        if self.sequence[-1] in self.notches and self.next is not None:
            self.next.rotate()
