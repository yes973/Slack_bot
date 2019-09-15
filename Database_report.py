# -*- coding: utf-8 -*-

import psycopg2
import pandas as pd
import numpy as np
from numpy import nan as NA
from pandas import Series,DataFrame
from datetime import datetime
from collections import Counter
from slacker import Slacker

conn_string = "host='000.000.000.000' dbname ='your_dbname' user='your_username' password='your_password'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()
cur.execute("SELECT * FROM Your_query")
output_dataframe = pd.DataFrame(cur.fetchall())
cur.close()
conn.close()

output_dataframe.columns = ['전년동기','전월동기','KPI']
output_dataframe.index = ['신규유저', '활동유저','매출합계(원)']

token = 'your_slack_token'
slack = Slacker(token)
slack.chat.post_message('#your_channel', '주기적으로 제공되는 KPI YoY입니다.\n'+str(output))
