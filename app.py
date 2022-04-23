# -*- coding: utf-8 -*-
"""streamlit_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zaX6bEMARA4H1C5dJZ0PZC3KN9b2p7OE

import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
"""

#!pip install pystan

"""
from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation
from fbprophet.diagnostics import performance_metrics
"""

#! pip install streamlit -q

#%%writefile app.py
import streamlit as st

import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')

#!pip install pystan

from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation
from fbprophet.diagnostics import performance_metrics

from fbprophet.plot import plot_plotly
import plotly.offline as py

items = []
for i in range(1, 51):
  items.append(str(i))


df = pd.read_csv('/content/item_forecast.csv')
df1 = pd.pivot_table(df, values = "sales", index="date", columns = "item", aggfunc = np.sum)

df1.columns = [ 'item_' + str(i) for i in range(1,len(df1.columns)+1)]
df1 = df1.reset_index()

def data(item_number):
  item_data = {"ds": [], "y": []}

  for i in range(len(df1)):
    if len(df1[i:i+90])==90:
      item_data["ds"].append(df1['date'][i])
      item_data["y"].append(df1[item_number][i:i+90].sum())
  item_data = pd.DataFrame(item_data)
  return item_data

def model_fit(item_number):
  #Calling the dataframe for specific item
  item_data = data(item_number) #Function call - data(item_number)
  train, test = item_data[item_data['ds'] <= '2016-12-31'], item_data[item_data['ds'] > '2016-12-31']
  model = Prophet(interval_width = 0.80, changepoint_range = 0.9)
  #model = Prophet(changepoint_range=0.9)
  model.fit(train)

  return item_data, train, test, model

# Model prediction - Main function -> This includes data aggregation function and model fitting function.
def model_prediction(item_number, periods):
  # Calling model_fit function
  item_data, train, test, model = model_fit(item_number)
  future_dates = model.make_future_dataframe(periods = periods)
  forecast = model.predict(future_dates)
  return item_data, train, test, model, forecast



st.title("Item Demand forecasting")
st.write("Select the item and tenure")
item_number = st.selectbox('Select Item number', tuple(items))
periods = st.slider('Future prediction date between 90-365', min_value = 90, max_value = 365, step = 1)
st.write("Future prediction period: ", periods)


if st.button("Predict Sales"):
  item_data, train, test, model, forecast = model_prediction('item_' + item_number, periods)
  fig = plot_plotly(model, forecast) # Prophet's plot method creates a prediction graph
  st.write(fig)

#!streamlit run app.py & npx localtunnel --port 8501



















