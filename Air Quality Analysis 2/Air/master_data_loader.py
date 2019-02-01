



#|| CO-4 || OZONE-5 ||  NO2-6 || SO2-7 || PM2.5-8 || TEMP-9 || CO_AQI-10 OZONE_AQI-11 || NO2_AQI-12 || SO2_AQI-13 || PM2.5_AQI- 14 || AVG_AQI-15

#print(p.system_accuracy())
#MASTER DATA FRAME WILL ALWAYS HAVE ALL THE DATA THAT WAS LOADED. DATA WILL GET APPENDED TO THIS DF FOR FUTHER ANALYSIS
class master_data_loader:
	import pandas as pd
	from pandas import DataFrame as df
	import numpy as np
	def __init__(self):
		import pandas as pd
		self.master_data=pd.read_csv("masterdata.csv")
		self.master_data.drop_duplicates()

	def append_master_data(self,path):
		import pandas as pd
		new_data = pd.read_csv(path)
		frame=[self.master_data,new_data]
		new_master_data = pd.concat(frame,axis=0,ignore_index=True)
		new_master_data.to_csv("masterdata.csv", sep=',', encoding='utf-8',index=False)
		return new_master_data
	
	def get_master_data(self):
		return self.master_data

m=master_data_loader()
m.append_master_data("2015final.csv")
m.append_master_data("2016final.csv")