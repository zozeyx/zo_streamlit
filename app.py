!pip install --upgrade pip
import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(500,2) / [50,50] + [37.76, -122.4],colums = ['lat', 'lon'])
st.map(df)
                                                                       
