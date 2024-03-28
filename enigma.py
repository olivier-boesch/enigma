"""
Enigma Machine class

Olivier Boesch - 2024
"""
import string
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector


class Enigma(object):
    """
    Enigma Machine class to encode/decode text
    """
    def __init__(self, plug_board_couples: list[str] | None = None,
                 rotors_models: list[str] | None = None,
                 rotors_start_sequence: str = "",
                 reflector: str = "") -> None:
        """
        Create machine object
        :param plug_board_couples: list of str for exchanging letter of plugboard
        :param rotors_models: list of rotor names
        :param reflector: name of the reflector
        :param rotors_start_sequence: initial letter positions of the rotors
        """
        # create the plugboard
        plugboard_object = Plugboard(plug_board_couples)
        # check if rotors ans rotors_start_sequence are consistent
        if len(rotors_start_sequence) != len(rotors_models):
            raise Exception("start sequence is too short or too long")
        # copy and reverse the rotors names (given L to R and switch R to L)
        rotors_models = rotors_models.copy()
        rotors_models.reverse()
        # reverse the start sequence of rotors as well
        rotors_start_sequence = rotors_start_sequence[::-1]
        # create rotors
        rotors_objects = [Rotor(model_name=rotors_models[i], start_letter=rotors_start_sequence[i])
                          for i in range(len(rotors_models))]
        # create the reflector
        reflector_object = Reflector(name=reflector)
        # ----------- build machine structure
        # plugboard at first
        self.machine_structure = plugboard_object
        # connect the rotors
        for i in range(1,len(rotors_objects)):
            rotors_objects[i-1].next = rotors_objects[i]
            rotors_objects[i].previous = rotors_objects[i-1]
        # connect right rotor with the plugboard (first one)
        plugboard_object.next = rotors_objects[0]
        rotors_objects[0].previous = plugboard_object
        # connect the reflector with the left rotor (last one)
        rotors_objects[-1].next = reflector_object
        reflector_object.previous = rotors_objects[-1]

    def encode_text(self, text: str) -> str:
        """
        Encode text / decode text with the machine
        :param text: text to encode / decode
        :return: encoded / decoded text
        """
        text = text.upper()  # convert to uppercase
        encoded_text = ""
        for letter in text:
            # encode only if the character is an uppercase letter
            if letter in string.ascii_uppercase:
                # encode the letter
                encoded_text += self.machine_structure.encode_forward(letter)
                # rotate after each encoding
                self.machine_structure.rotate()
            # otherwise copy it
            else:
                encoded_text += letter
        return encoded_text

    # encode and decode are the same operation
    decode_text = encode_text

    def __str__(self):
        """
        String representation of the machine structure and state
        :return:
        """
        current = self.machine_structure
        output_text = "-------------------------------------\n"
        output_text += "Enigma Machine - Structure and state (Rotors are given Right to Left):\n"
        while current is not None:
            output_text += str(current) + "\n"
            current = current.next
        output_text += "-------------------------------------"
        return output_text


if __name__ == "__main__":
    print("Run main.py for tests")