# encoding=utf-8


import tushare as ts
import time as tm
from sqlalchemy import create_engine
import pandas as pd

tmstr = tm.strftime("%Y-%m-%d", tm.localtime())
engine = create_engine('mysql+pymysql://allen:qin88min@192.161.180.105/stock?charset=utf8')

# 个股首个上市日期
df = ts.get_stock_basics() # type: pd.DataFrame


print(df)

# 存数据
df.to_sql('stock_basics', engine, if_exists='append', index=True)
# encoding=utf-8

