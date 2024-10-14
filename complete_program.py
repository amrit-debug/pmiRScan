import subprocess
import sys
import pandas as pd
from sys import argv



if sys.version_info[0] < 3: 
	from StringIO import StringIO
else:
	from io import StringIO
	
	

class genstats:
	def inp(self, X):
		arr_char = []
		line = X
		for ch in line:
			arr_char.append(ch)
		bases = ['A' ,'U', 'G', 'C', 'T', 'a', 'g', 'c', 'u', 't']
		res = all(ele in bases for ele in arr_char)
		if res == True:
			f = lambda x: x.replace('T', 'U')
			arr_char = list(map(f, arr_char))
			self.seq = ''.join(map(str,arr_char))
			return self.seq
		else:
			print("Sequences contain invalid characters!")
			exit()
	
