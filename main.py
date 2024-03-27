from enigma import Enigma

# ENIGMA MACHINE TEST CONFIG
enigma_config = {
    # plug board associations (A<->E and B<->T)
    "plug_board_couples": ["AE", "BT", "ZV"],
    # ROTORS (first rotor: model=I, starts at A, second rotor: model: II, starts at B, ...)
    "rotors": ["I", "III", "V", "IV"],
    "rotors_start_sequence": "DGHZ",
    # REFLECTOR (model: C thin model)
    "reflector": "C-thin"
}


# MESSAGE TO ENCODE
print("message to encode")
message = """The Enigma machine is a cipher device developed and used in the early- to mid-20th century to protect commercial, diplomatic, and military communication. It was employed extensively by Nazi Germany during World War II, in all branches of the German military. The Enigma machine was considered so secure that it was used to encipher the most top-secret messages.
The Enigma has an electromechanical rotor mechanism that scrambles the 26 letters of the alphabet. In typical use, one person enters text on the Enigma's keyboard and another person writes down which of the 26 lights above the keyboard illuminated at each key press. If plain text is entered, the illuminated letters are the ciphertext. Entering ciphertext transforms it back into readable plaintext. The rotor mechanism changes the electrical connections between the keys and the lights with each keypress.
The security of the system depends on machine settings that were generally changed daily, based on secret key lists distributed in advance, and on other settings that were changed for each message. The receiving station would have to know and use the exact settings employed by the transmitting station to successfully decrypt a message. """
print(message)
# create encoding enigma machine
print()
print("Create encoding machine")
enigma = Enigma(**enigma_config)
# print startup config and state
print()
print("initial machine state and config")
print(enigma)
# encode
print()
print("encoding message")
res = enigma.encode_text(message)
# print end config and state
print()
print("final machine state and config")
print(enigma)
# print encoded text
print()
print("encoded message")
print(res)

# -----------------------------

# create decoding enigma machine
print("--------------------------------------------------------------")
print("Create decoding machine")
enigma2 = Enigma(**enigma_config)
# print startup config and state
print()
print("initial machine state and config")
print(enigma2)
# decode encrypted text (same as encode) and print
print()
print("decode and print message")
print(enigma2.decode_text(res))
# print end config and state
print()
print("final machine state and config")
print(enigma2)

