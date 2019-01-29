import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
st=dt.date(2000,1,1)
en=dt.date.today()

df=web.DataReader('TSLA','yahoo',st,en)
print(df.head())
