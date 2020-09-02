# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 01:12:31 2020

@author: mihika.s-v
"""

import numpy as np
import pandas as pd
from datetime import datetime

#reading the file
df = pd.read_csv (r'C:\Users\mihika.s-v\Desktop\INDVideos.csv')

#creating a new column for pipe separated text
df['new_tag'] = df['tags'].str.split('|').str[2]

#creating new column for month
df['Month'] = pd.DatetimeIndex(df['publish_time']).month

#creating new column for year
df['Year'] = pd.DatetimeIndex(df['publish_time']).year

#creating new data file with derived columns
df.to_csv(r'C:\Users\mihika.s-v\Desktop\data_python.csv')