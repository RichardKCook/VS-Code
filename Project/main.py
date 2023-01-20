import pandas as pd
from yahoo_fin import stock_info
from plotly.offline import plot
from plotly.offline import init_notebook_mode
init_notebook_mode()
import plotly
import cufflinks as cf
cf.set_config_file(offline=True)
setattr(plotly.offline, "__PLOTLY_OFFLINE_INITIALIZED", True)
from functions import boll_print
from functions import boll



# Get the data
data = {}
data['AAPL'] = stock_info.get_data('GOOG', start_date='01-01-2022',  end_date='01-28-2023')
# print(data['AAPL'].head())
# print(data["AAPL"])

# qf = cf.QuantFig(data['AAPL'])
# qf.add_bollinger_bands(boll_std=2)
# qf.add_macd()
# qf.add_rsi()
# qf.add_dmi()
# qf.iplot()

i = boll_print(data['AAPL']['close'], include= False, length=14, fillna=True)

j = boll(data['AAPL']['close'], include= False, length=14, fillna=True)

print(j)

if i[2].any() < i[0].all():
    print("Sell")