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

df = pd.read_csv(resource_path('athlete_events.csv'))
region_df = pd.read_csv(resource_path('noc_regions.csv'))

df=df[df['Season']=='Summer']
# merge with region_df
df=df.merge(region_df,on='NOC',how='left')
# dropping duplicates
df.drop_duplicates(inplace=True)
# for medals
pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
df=pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
