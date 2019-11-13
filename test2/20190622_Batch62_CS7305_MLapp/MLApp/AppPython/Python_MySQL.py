import os
import numpy as np
import pandas as pd
import configparser

PATH = os.getcwd()

config = configparser.ConfigParser()
config.read(PATH+'/conf/config.ini')

host        = config['MySQL']['host']
port        = config['MySQL']['port']
user        = config['MySQL']['user']
password    = config['MySQL']['password']
db          = config['MySQL']['db']

connector = 'mysql+mysqlconnector://' + user + ':' + password + '@' + host + ':' + port + '/' + db

bank = pd.read_sql("select * from bank", con=connector)

print(bank.head(4))

bank.replace(to_replace=['unknown'], value=np.nan, inplace=True)

print(bank.head(4))

# customer_no is not of much value to dropping it
bank = bank.drop(['customer_no'], axis=1)

print(bank.head(4))