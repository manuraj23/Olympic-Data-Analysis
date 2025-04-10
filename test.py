import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go
import preprocessor
import helper
import os,sys
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
df = pd.read_csv(resource_path('athlete_events.csv'))
region_df = pd.read_csv(resource_path('noc_regions.csv'))

df=preprocessor.preprocess(df,region_df)

# Group by 'product name' and sum the 'sales' for each product
total_sales_by_product = df.groupby('Name')['total'].sum()

print(total_sales_by_product)
