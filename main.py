#!/usr/bin/env python3
import os
from evdev import InputDevice, list_devices, ecodes as e
import importlib

def find_device_by_name(target_name):
    for path in list_devices():
        device = InputDevice(path)
        if target_name.lower() in device.name.lower():
            print(f"✅ Found device: {device.name} at {path}")
            return path
    print(f"❌ Device '{target_name}' not found.")
    return None

# --- Load profile dynamically ---
profile_name = os.getenv("BEAUTY_PROFILE", "default_profile")
profile_module = importlib.import_module(f"profiles.{profile_name}")

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

button_actions = {
    "TOP": getattr(profile_module, "top_click"),
    "LEFT": getattr(profile_module, "left_click"),
    "BOTTOM": getattr(profile_module, "bottom_click"),
    "RIGHT": getattr(profile_module, "right_click"),
    "MIDDLE": getattr(profile_module, "middle_click"),
    "CAMERA": getattr(profile_module, "camera_click")
}

for event in dev.read_loop():
    if event.type == e.EV_REL:
        key_name = REL_TO_KEY.get(event.value)
        if key_name in button_actions and key_name != last_identified:
            button_actions[key_name]()
            last_identified = key_name
    elif event.type == e.EV_KEY and event.code == e.BTN_LEFT:
        last_identified = None
