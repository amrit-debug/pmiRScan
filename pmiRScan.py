import subprocess
import sys
import numpy as np
import pandas as pd
from sys import argv
import complete_program as cpm
import triplet_svm_features as tpsvm
import RNAfold_params as rnf
import number_of_loops as numl
import count_indi_bp as cbp
import other_features as cmb
import time
import training_sequence as bgm
from training_sequence import *
from training_sequence import x_train, y_train
from sklearn.preprocessing import Normalizer


if sys.version_info[0] < 3: 
	from StringIO import StringIO
else:
	from io import StringIO
	
input_file = str(argv[1])
output_file = str(argv[2])
with open("./data/" + input_file,'r') as f1:
	nuc = f1.readlines()
sequences = []
for lin in nuc:
	lin = lin.strip()
	if lin.startswith(">"):
		continue
	else:
		cpgm = cpm.genstats()
		cpgm.inp(lin) 
		

def main(*args):
	print(args)
	
print("calculating sequential features...")
if __name__ == "__main__":
	res = subprocess.Popen(["perl", "genRNAStats.pl", "-i", input_file], stdout=subprocess.PIPE)
res1 = StringIO(res.communicate()[0].decode('utf-8'))

df = pd.read_csv(res1, sep = "\t")
df = df.drop(['Unnamed: 92'], axis = 1)

time.sleep(2)


#Secondary structurural features
print("calculating structural features...")
if __name__ == "__main__":
	result = subprocess.Popen(["RNAfold", "-d2", "--noLP", "--noPS", "--noDP", "--MEA", "-p", "-i", input_file], cwd = "./data/", stdout = subprocess.PIPE)
result1 = StringIO(result.communicate()[0].decode('utf-8'))
content = result1.getvalue()

with open("out.txt", "wb") as cmd_file:
	cmd_file.write(content.encode('utf-8'))
	

with open("out.txt", "r") as f1:
	x = f1.readlines()

i=0
tp_svm = tpsvm.trip_svm()
df = tp_svm.triplet_svm(x,df)


time.sleep(2.5)

notation = x[2]
count = 0

number_loops = numl.loops()
df = number_loops.loop_number(x, notation, df)


indi_count = cbp.ind_bp()
df = indi_count.individual_bp(x, df)

combined_features = cmb.combined()
df = combined_features.comb_features(df)

df.to_csv("./results/all_features.csv", index=False)


# Prediction of pre-miRNAs
print("predicting pre-miRNAs...")


premir_df = pd.read_csv("./results/all_features.csv", low_memory = False)
premir_df = premir_df[premir_df.columns[1:]]
x_input = premir_df[['%AA', '%AU', '%GC', '%GG', '%GU', '%UA', '%UG', '%AAC', '%AAU', '%CAA', '%CAG', '%CUG', '%GCU', 
'%GGC', '%GUG', '%UGC', '%UGG', 'Npb', 'Nmfe', 'NQ', 'A..(', 'A...', 'U...', 'G...', 'C...', 
'%(G-C)/n_stems', '%(A-U)/n_stems', '%(G-U)/n_stems']]
       
x_input.to_csv("./results/selected_features.csv", sep = ",", index=False)
       
scaler = Normalizer()
scaled_data = scaler.fit_transform(x_input)
x_input = pd.DataFrame(scaled_data,
                         columns=x_input.columns)
                         
bg = bgm.ligbm()
y_p = bg.lgb_classifier(x_train, y_train, x_input)



input_file=argv[1]


ones = []
zeroes = []
for item in range(0, len(y_p)):
	if(y_p[item] == 0):
		zeroes.append(item)
	else:
		ones.append(item)

sequences = []

input_file="./data/" + str(argv[1])
with open(input_file,'r') as f2:
	nuc = f2.readlines()
	for line in nuc:
		if line.startswith(">"):
			sequences.append(line)



results = []
head = "Sequence ID,Prediction"
results.append(head)
for element in range(0, len(sequences)):
	if element in zeroes:
		out = (str(sequences[element]).upper().strip("\n")) + ",Not a pre-miRNA"
		results.append(out)
	elif element in ones:
		out = (str(sequences[element]).upper().strip("\n")) + ",pre-miRNA"
		results.append(out)
	else:
		break
		
with open("./results/" + output_file + ".xls", 'w') as r1:
	r1.write("\n".join(results))
	
print("Done!")
