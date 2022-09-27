#!/bin/python3
#
import os
import sys
import sqlite3
# importing panda library
import pandas as pd
  
# readinag given csv file
# and creating dataframe
dataframe1 = pd.read_csv("bon15001.dat",header = None,skiprows=2)
  
print(dataframe1)
