#!/usr/bin/env python3
from evdev import ecodes as e

def top_click(ui):
    print("TOP pressed (OnlineGDB)")

def left_click(ui):
    print("LEFT pressed (OnlineGDB)")

def bottom_click(ui):
    print("BOTTOM pressed (OnlineGDB)")

def right_click(ui):
    print("RIGHT pressed (OnlineGDB)")

def middle_click(ui):
    # Enter key
    ui.write(e.EV_KEY, e.KEY_ENTER, 1)
    ui.write(e.EV_KEY, e.KEY_ENTER, 0)
    ui.syn()

def camera_click(ui):
    # F9 key (Run/Debug)
    ui.write(e.EV_KEY, e.KEY_F9, 1)
    ui.write(e.EV_KEY, e.KEY_F9, 0)
    ui.syn()
