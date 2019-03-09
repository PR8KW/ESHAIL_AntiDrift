# coding: utf8

#############################################################################
# show-audio-devices.py v0.1 by Harald Maiss, DL3HM
#
# show all available audio devices for configuration of anti-drift.py
#############################################################################

# Libraries which need to be intalled with pip on a plain Python system

# https://python-sounddevice.readthedocs.io/en/0.3.12/index.html
# Install: pip install sounddevice
import sounddevice as sd


print(sd.query_devices())

input("Press <RETURN> to quit!")
