import numpy as np
import pandas as pd

	
class trip_svm():
	def triplet_svm(self, x, df):
		seq = []
		for line in range(0,len(x)):
			if(line%7==1):
				SQ_not = [x[line], x[line+1]]
				seq.append(SQ_not)   

		df1 = pd.DataFrame()
		words = ['A(((', 'A((.', 'A(..', 'A(.(', 'A.((', 'A.(.', 'A..(', 'A...', 'U(((', 'U((.', 'U(..', 'U(.(', 'U.((', 
		'U.(.', 'U..(', 'U...', 'G(((', 'G((.', 'G(..', 'G(.(', 'G.((', 'G.(.', 'G..(', 'G...', 'C(((', 'C((.', 'C(..', 
		'C(.(', 'C.((', 'C.(.', 'C..(', 'C...']

		el = []
		for word in words:
			for element in seq:
				count = 0
				sq = element[0]
				ntn = element[1]
				for i in range(len(sq)-3):
					trip = str(sq[i]) + str(ntn[i+1:i+4])
					if trip == word:
						count += 1
						i += 1
				el.append(count)
			df1[str(word)] = el
			el.clear()

		frames = [df, df1]
		df = pd.concat(frames, axis=1)
		return df

