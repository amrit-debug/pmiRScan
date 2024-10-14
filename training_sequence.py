import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import lightgbm as lgb
from lightgbm import LGBMClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE


premir_df = pd.read_csv("training_set12_3.csv", sep = ',')
premir_df['Category'] = premir_df['Category'].map({'Pre-mir': 1, 'Pseudo-premir': 0})
premir_df = premir_df.dropna()

feature_df = premir_df[['%AA', '%AU', '%GC', '%GG', '%GU', '%UA', '%UG', '%AAC', '%AAU', '%CAA', '%CAG', '%CUG', '%GCU', 
'%GGC', '%GUG', '%UGC', '%UGG', 'Npb', 'Nmfe', 'NQ', 'A..(', 'A...', 'U...', 'G...', 'C...', 
'%(G-C)/n_stems', '%(A-U)/n_stems', '%(G-U)/n_stems']]       


X = feature_df
Y = premir_df['Category']





X, Y = SMOTE(random_state = 5).fit_resample(X, Y)
scaler = Normalizer()
scaled_data = scaler.fit_transform(X)
X = pd.DataFrame(scaled_data,
                         columns=X.columns)



x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify = Y, random_state = 5)

class_counts = y_train.value_counts()
total_samples = len(y_train)


class_weights = {cls: total_samples / count for cls, count in class_counts.items()}

class ligbm():
	def lgb_classifier(self, X, Y, x):

		
		lgb_model = lgb.LGBMClassifier(n_estimators = 100, random_state=5, boosting_type = 'gbdt', max_bin = 10000, 
										num_leaves = 200, learning_rate = 0.1, objective = 'binary', min_data_in_leaf = 20, 
										feature_fraction = 0.7,bagging_fraction = 0.7, bagging_freq = 20, verbosity = -1)
		lgb_model.fit(X,Y)
		y_pred = lgb_model.predict(x)
		y_p = []
		for item in y_pred:
			y_p.append(item)
		self.y_p = y_p
		return self.y_p
		
