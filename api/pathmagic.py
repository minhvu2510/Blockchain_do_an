"""
    Config PYTHON PATH for project to load sub-module
"""

import os
import sys


cwd = os.getcwd()
parent_cwd = os.path.split(cwd)[0]
sys.path.append(parent_cwd)
