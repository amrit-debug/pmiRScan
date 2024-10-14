import pandas as pd

class ind_bp():
	def individual_bp(self, x, df):
		text=[]
		index_couples=[]
		char_couples=[]
		CG = []
		AU = []
		GU = []


		i=0
		for line in range(0, len(x)):
			if(line%7==1):
				text = [str(x[line]),str(x[line+1])]
				
				indexing = []


				temp_index_couples=[]
				temp_char_couples=[]
				sublist_char=text[0].strip()
				sublist_brac=text[1].strip()
				sublist_brac = sublist_brac.split()
				sublist_brac = sublist_brac[0]
				indices = []
				for char in range(len(sublist_brac)):
					if((sublist_brac[char] == '(') or (sublist_brac[char] == ')')):
						indices.append(char)
					indexing.append(indices)
					count_A = 0
					count_G = 0
					count_C = 0
					count_U = 0
					rest_G = 0
					rest_U = 0
					GU_pair = 0
					
					for item in indices:
						if(sublist_char[item] == 'G'):
							count_G += 1
						elif(sublist_char[item] == 'C'):
							count_C += 1
						elif(sublist_char[item] == 'A'):
							count_A += 1
						elif(sublist_char[item] == 'U'):
							count_U += 1
						else:
							break
					
					if (count_C == count_G):
						CG_pair = count_C
						
						
					else:
						CG_pair = count_C
						rest_G = count_G - count_C
						
					if(count_A == count_U):
						AU_pair = count_A
						
					else:
						AU_pair = count_A
						rest_U = count_U - count_A
						
					if(rest_G == rest_U):
						GU_pair = rest_G
						
				
				CG.append(CG_pair)
				AU.append(AU_pair)
				GU.append(GU_pair)
						

		df1 = pd.DataFrame({'(G-C)': CG, '(A-U)': AU, '(G-U)': GU})


		frames = [df, df1]
		df = pd.concat(frames, axis =1)
		return df
