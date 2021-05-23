#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    word = s.split(' ')
    return (' '.join((x.capitalize() for x in word)))

# things didnt work for me -
  # Tried using title() - have its own limitations
  # tried using capwords from string library - limitations for string having special characters
  # tried using upper() - capitalizes whole string
