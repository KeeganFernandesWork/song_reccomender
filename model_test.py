import joblib

loaded_scaler = joblib.load('preprocessor.joblib')
loaded_model = joblib.load('model.joblib')

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

prediction = loaded_model.predict(val)[0]
print(prediction)
