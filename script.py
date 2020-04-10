# Refactor Sort Imports and it also sorts third party libraries

from os import rename
import math
import os
import sys

import requests

# print sys.version  # Shows pylint working
# print(sys.version)  # Which version of python
# print(sys.executable)  # Where it's located


def greet(who_to_greet):
    greeting = f'Hello, {who_to_greet}'
    return greeting


# print(greet('World'))
# print(greet('Steve'))

"""
Bottom Left Corner lets you pick your interpreter
Right click run python file in terminal
In the .vs code file it sets folder specific configs but you can change global settings 13:09 mark voideo.
Colour these for exapmle command palette COMMAND SHIFT P and search colour
Predawn colour theme.
Icon theme as well Ayu
To do the setting changes we can click the gear in the bottom left and go into settings
Setting Up the Settings and Configs
However you might want the user settings to be different to teh global settings for a project for the purposes
Of virtual environments
python3 -m venv venv33   Creating the virtual environment
Choose it as the python interpretetr for this project
"""

# print(sys.version)  # Which version of python
print(sys.executable)  # Where it's located
#r = requests.get('https://coreyms.com')
# print(r.status_code)

# Install Black as the autoformatter Shift Option F
"""
Installation - 1:13
Python Extension - 5:48
Switching Interpreters - 10:04
Changing Color Themes - 12:35
VSCode Settings - 16:16
Set Default Python - 21:33
Using Virtual Environments - 25:10
IntelliSense - 29:45
Code Formatting - 32:13
Code Linting - 37:06
Code Runner Extension - 39:42
Git Integration - 47:44
Use Different Terminal - 51:07
Debugging - 58:45
Unit Testing - 1:03:25
Zen Mode - 1:09:55
"""


# Install the Coderunner extension toa utomatically
# run code and configure it to run the version of pyton youre using not the default
# The code runner documentation shows you how to configure it
# Now uses virtual environment, clears previous output and clean output
#    "code-runner.showExecutionMessage": false,
#   "code-runner.clearPreviousOutput": true
# Control Option N also hits run

# Working with input 48:28

#name = input("Your name? ")
# Don't run code run in terminal when it comes to input
#print(f"Hello {name}.")


# Built in Git integration, create the gitignore file 50:50
