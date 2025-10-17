#!/usr/bin/env python3
from evdev import InputDevice, ecodes as e

DEVICE_PATH='/dev/input/event23'    
dev = InputDevice(DEVICE_PATH)

REL_TO_KEY = {
    77: "TOP",
    80: "LEFT",
    -76: "BOTTOM",
    -80: "RIGHT",
    -375: "MIDDLE",
    -30: "CAMERA"
}

last_identified = None

def press_f9():
    ui.write(e.EV_KEY, e.KEY_F9, 1)
    ui.write(e.EV_KEY, e.KEY_F9, 0)
    ui.syn()
    
def press_enter():
    ui.write(e.EV_KEY, e.KEY_ENTER, 1)  # key press
    ui.write(e.EV_KEY, e.KEY_ENTER, 0)  # key release
    ui.syn()

button_actions = {
    "TOP": lambda: print("TOP pressed"),
    "LEFT": lambda: print("LEFT pressed"),
    "BOTTOM": lambda: print("BOTTOM pressed"),
    "RIGHT": lambda: print("RIGHT pressed"),
    "MIDDLE": lambda: print("MIDDLE pressed"),
    "CAMERA": lambda: print("CAMERA pressed")
}

for event in dev.read_loop():
    if event.type == e.EV_REL:
        key_name = REL_TO_KEY.get(event.value)
        if key_name in button_actions and key_name != last_identified:
            button_actions[key_name]()
            last_identified = key_name
    elif event.type == e.EV_KEY and event.code == e.BTN_LEFT:
        last_identified = None
