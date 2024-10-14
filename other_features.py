import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt




class combined():
	def comb_features(self, df):
		df['(G-C)/L'] = round(df['(G-C)']/df['Len'],6)
		df['(A-U)/L'] = round(df['(A-U)']/df['Len'],6)

		df['(G-U)/L'] = round(df['(G-U)']/df['Len'],6)

		df['%(G-C)/n_stems'] = round((df['(G-C)/L'] * 100)/df['number_of_loops'],4)

		df['%(A-U)/n_stems'] = round((df['(A-U)/L'] * 100)/df['number_of_loops'],4)


		df['%(G-U)/n_stems'] = round((df['(G-U)/L'] * 100)/df['number_of_loops'],4)
		df = df.drop(['Len', '(G-C)', '(A-U)', '(G-U)', 'number_of_loops', '(G-C)/L', '(A-U)/L', '(G-U)/L'], axis=1)



		df1 = df.copy()

		return df
