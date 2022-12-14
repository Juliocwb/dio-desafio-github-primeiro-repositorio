# -*- coding: utf-8 -*-
"""PythonMachinelearnig.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fuH25w3aUXmzeDJvx13BGFqPkzZVXZgR
"""

import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

url = 'https://github.com/neylsoncrepalde/projeto_eda_covid/blob/master/covid_19_data.csv?raw=true'

df = pd.read_csv(url, parse_dates=['ObservationDate', 'Last Update'])
df

df.dtypes

import re

def corrige_colunas(col_name):
    return re.sub(r"[/|| ]","",col_name).lower()

corrige_colunas("Adge/P ou")

df.columns = [corrige_colunas(col) for col in df.columns]

df

df.loc[df.countryregion == 'Brazil']

brasil = df.loc[
    (df.countryregion == 'Brazil') &
    (df.confirmed >0)
]

brasil

px.line(brasil, 'observationdate', 'confirmed', title='Caso confirmado no Brasil')

brasil['novoscasos']= list(map(
    lambda x: 0 if (x==0) else brasil['confirmed'].iloc[x] - brasil['confirmed'].iloc[x-1],
    np.arange(brasil.shape[0])
))

brasil

px.line(brasil, x='observationdate', y='novoscasos', title='Novos Casos por dia')

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=brasil.observationdate, y=brasil.deaths, name='Mortes',
               mode='lines+markers', line={'color' : 'red'})
)
fig.update_layout(title='Mortes por COVID-19 no Brasil')
fig.show()

def taxa_crescimento(data, variable, data_inicio=None, data_fim=None):
    if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable] > 0].min()
    else:
        data_inicio = pd.to_datetime(data_inicio)
    if data_fim == None:
        data_fim = data.observationdate.iloc[-1]
    else:
        data_fim = pd.to_datetime(data_fim)

    passado = data.loc[data.observationdate == data_inicio, variable].values[0]
    presente = data.loc[data.observationdate == data_fim, variable]. values[0]

    n= (data_fim - data_inicio).days

    taxa = (presente/passado) **(1/n) -1

    return taxa*100

taxa_crescimento(brasil, 'confirmed')

def taxa_crescimento_diaria( data, variable, data_inicio=None):
  if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable] > 0].min()
  else:
      data_inicio = pd.to_datetime(data_inicio)
  
  data_fim = data.observationdate.max()

  n= (data_fim - data_inicio).days


  taxas = list(map(
      lambda x: (data[variable].iloc[x] - data[variable].iloc[x-1]) / data[variable].iloc[x-1],
      range(1, n+1)
  ))

  return np.array(taxas) *100

tx_dia = taxa_crescimento_diaria(brasil, 'confirmed')

tx_dia

primeiro_dia = brasil.observationdate.loc[brasil.confirmed > 0].min()

px.line(x=pd.date_range(primeiro_dia, brasil.observationdate.max())[1:],
        y=tx_dia, title='Taxa de crescimento de casso confirmados no brasil')

from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

confirmados = brasil.confirmed
confirmados.index = brasil.observationdate
confirmados

res = seasonal_decompose(confirmados)

fig, (ax1, ax2, ax3, ax4,) = plt.subplots(4, 1, figsize=(10, 8))

ax1.plot(res.observed)
ax2.plot(res.trend)
ax3.plot(res.seasonal)
ax4.plot(confirmados.index, res.resid)
ax4.axhline(0, linestyle = 'dashed', c='black')
plt.show()

pip install pmdarima

from pmdarima.arima import auto_arima
modelo = auto_arima(confirmados)

fig = go.Figure(go.Scatter(
    x=confirmados.index, y=confirmados, name='Observados'
))

fig.add_trace(go.Scatter(
    x=confirmados.index, y=modelo.predict_in_sample(), name='Preditos'
))

fig.add_trace(go.Scatter(
    x=pd.date_range('2020-05-20', '2020-06-20'), y=modelo.predict(31), name='Forecast'
))

fig.update_layout(title="Preveisao de casos confirmado no brasil para proximos 600 dias")
fig.show()

conda install -c conda-forge fbprophet -y

