# provide mappings from raylib to a consistent name
import raylib as rl

def extract_consts(prefix):
    names = list(filter(lambda x: x.startswith(prefix), dir(rl)))
    return set(getattr(rl, name) for name in names)

keyboard_key = extract_consts('KEY_')
mouse_button = extract_consts('MOUSE_BUTTON_')
gamepad_button = extract_consts('GAMEPAD_BUTTON_')
gamepad_axis = extract_consts('GAMEPAD_AXIS_')
