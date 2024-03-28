# Enigma Machine Simulator

## Architecture

Each component of the machine has its own class

### PlugBoard: The Plug Board

### Rotor: The Rotor

### Reflector : The Reflector

### Enigma : The machine itself

usage:
```python
# A Kriegmarine enigma with 4 rotors
enigma_config = {
    # plug board associations (A<->E,  B<->T and Z<->V)
    "plug_board_couples": ["AE", "BT", "ZV"],
    # ROTORS (first rotor: model=I, starts at D, second rotor: model: III, starts at G, ...)
    "rotors_models": ["I", "III", "V", "IV"],
    "rotors_start_sequence": "DGHZ",
    # REFLECTOR (model: C thin model)
    "reflector": "C-thin"
}

message = "hello world"

enigma = Enigma(**enigma_config)

encoded_message = enigma.encode_text(message)

```