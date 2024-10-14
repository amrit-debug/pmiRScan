#from RNAfold_params import df
import numpy as np
import pandas as pd



class loops():
	def loop_number(self, x, notation, df):
		nlp = []
		for line in range(0, len(x)):
			count = 0
			if (line%7==2):
				notation = x[line]
				for i in range(len(notation)-1):
					char = str(notation[i]) + str(notation[i+1])
					if (char == ")("):
						count += 1
					else:
						continue
				num_loops = count + 1
				nlp.append(num_loops)
			else:
				continue
				
		df1 = pd.DataFrame({"number_of_loops":nlp})
		frames = [df, df1]
		df = pd.concat(frames, axis = 1)
		return df
