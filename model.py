import joblib
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
loaded_scaler = joblib.load('preprocessor.joblib')
loaded_model = joblib.load('model.joblib')
df = pd.read_csv("uri_labels.csv", dtype_backend='pyarrow', engine='pyarrow')

label = {0:"Sad", 1:"Happy", 2:"Energetic", 3:"Calm"}

values = {'duration (ms)':195000.0,
 'danceability': 0.611,
 'instrumentalness': 0.614,
 'speechiness':-8.815,
 'loudness': 0.0672,
 'valence': 0.0169,
 'spec_rate': 0.000794,
 'liveness':0.7530,
 'acousticness':0.520,
 'tempo':128.050,
 'energy':3.446154e-07}

from sklearn.feature_extraction import DictVectorizer
dictvectorizer = DictVectorizer(sparse=False)
features = dictvectorizer.fit_transform(values)
val = loaded_scaler.transform(features)

def predict(dic_val):
	val = dictvectorizer.fit_transform(dic_val)
	values = loaded_scaler.transform(val)#spotify:track:
	return loaded_model.predict(values)[0],label[loaded_model.predict(values)[0]]

def open_spotify(label):
	print(label)
	url = df[df["labels"] == label].sample(n = 1).uri.values[0]
	return url 
	

    
