import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact, IntSlider

"""defines a function to import and convert a file to csv format"""
def load_data(file):
    return pd.read_csv(file)

"""defines interactive slider component to make it easier to call forward later"""
def Int(min,max,step):
    return IntSlider(min=min, max=max, step=step, continuous_update=False)


