# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:03:53 2024

@author: lewis
"""

from  pathlib import Path
import os


current_dir = Path(os.getcwd())

data_files = os.path.join(current_dir.parents[0], "Data")


with open(os.path.join(data_files, "test.txt")) as f:
    for line in f:
        print(line)