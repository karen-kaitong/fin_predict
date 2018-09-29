import pandas as pd 
import numpy as np 
import argparse
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA

#add: identify seasonality/trend

#test_test_comment2
#select best arima model, output plot and prediction
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-i_fn', '--input_file_name', dest = 'input', \
		action = 'store', help = 'Read in data')
	parser.add_argument('-v', '--verbose', help = 'Display details about dastaset')
	#can pass in one date or two
	parser.add_argument('-sl', '--select', help = 'Select data based on the date')
	parser.add_argument('-pred', '--predict', help = 'Make prediction for next given period')
	parser.add_argument('-plot', action = 'store_true', help = 'Plot predicitons')
	parser.add_argument('-o_fn', '--output_file_name', help = 'Set output file name', \
		action= 'store', dest = 'output', default = 'prediction.csv')

	args = parser.parse_args()
	df = []
	prediction = []
	if args.input:
		df = pd.read_csv(arg.input).copy()
		#drop na
		df = df.dropna()
		df['datefield'] = pd.to_datetime(df['datefield'])
	if args.verbose:
		print(df.describe())
	if args.select:
		start = args.select[0]
		try:
			end = args.select[1]
		except:
			end = max(df['datefield'])
		df = df[(df['datefield'] >= start) & (df['datefield'] <= end)]
	if args.predict:
		rmse = 0
		#work in progress
		#choose best arima based on acf and pacf, print rmse and make prediction
		#for the given time period
		print('RMSE: {0}'.format(rmse))
	if args.plot:
		plt.plot(df['datefield'],df['pricefield'])
		prediction.plot(title = 'prediction')
		plt.show()
		plt.legend()
	if args.output:
		prediction.to_csv(args.output,index = False)

