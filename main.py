#!/usr/bin/python
import struct
import time
import sys
import gui

infile_path = "/dev/input/event0"

KEY_LEFTALT = 56
KEY_SPACE = 57

DOWN = 1
UP = 0

EVT_KEYPRESS = 1

#long int, long int, unsigned short, unsigned short, unsigned int
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

#open file in binary mode
in_file = open(infile_path, "rb")

event = in_file.read(EVENT_SIZE)

alt_down = False

while event:
    (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)

    if type == EVT_KEYPRESS:
        if value == DOWN:
            if code == KEY_LEFTALT:
                alt_down = True
            if code == KEY_SPACE and alt_down:
                g = gui.InputArea()
                g.show()

        if value == UP:
            if code == KEY_LEFTALT:
                alt_down = False

    event = in_file.read(EVENT_SIZE)

in_file.close()
