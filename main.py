#!/usr/bin/env python3
import os
from evdev import UInput, InputDevice, list_devices, ecodes as e
import importlib

# create a single UInput instance
ui = UInput()

def find_device_by_name(target_name):
    for path in list_devices():
        device = InputDevice(path)
        if target_name.lower() in device.name.lower():
            print(f"✅ Found device: {device.name} at {path}")
            return path
    print(f"❌ Device '{target_name}' not found.")
    return None

# --- Load profile dynamically ---
profile_name = os.getenv("BEAUTY_PROFILE", "default")
try:
    profile_module = importlib.import_module(f"profiles.{profile_name}")
except ModuleNotFoundError:
    print(f"❌ Profile '{profile_name}' not found. Falling back to default_profile.")
    profile_module = importlib.import_module("profiles.default_profile")

# --- Device setup ---
DEVICE_NAME = "Beauty-R1"
DEVICE_PATH = find_device_by_name(DEVICE_NAME)

if DEVICE_PATH:
    dev = InputDevice(DEVICE_PATH)
else:
    print("Exiting — device not found.")
    exit(1)

REL_TO_KEY = {
    77: "TOP",
    80: "LEFT",
    -76: "BOTTOM",
    -80: "RIGHT",
    -375: "MIDDLE",
    -30: "CAMERA"
}

last_identified = None

# Map button names to profile functions, passing ui
button_actions = {
    "TOP": lambda: profile_module.top_click(ui),
    "LEFT": lambda: profile_module.left_click(ui),
    "BOTTOM": lambda: profile_module.bottom_click(ui),
    "RIGHT": lambda: profile_module.right_click(ui),
    "MIDDLE": lambda: profile_module.middle_click(ui),
    "CAMERA": lambda: profile_module.camera_click(ui)
}
try:
    for event in dev.read_loop():
        if event.type == e.EV_REL:
            key_name = REL_TO_KEY.get(event.value)
            if key_name in button_actions and key_name != last_identified:
                button_actions[key_name]()
                last_identified = key_name
        elif event.type == e.EV_KEY and event.code == e.BTN_LEFT:
            last_identified = None

except KeyboardInterrupt:
    print("\nExiting… cleaning up.")
    ui.close()  # close the virtual input device
    dev.close()  # close the input device
