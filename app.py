from flask import Flask, render_template,request,redirect
from model import predict, open_spotify
import os
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
para = "Enter the Values of the Song that you want the model will classify the types and reccomend a song of the same variety"
arr = 0
@app.route('/', methods=['GET', 'POST'])
def home():
    inputs = ['valence', 'danceability', 'duration (ms)', 'loudness', 'spec_rate', 'liveness', 'energy', 'speechiness', 'tempo', 'acousticness', 'instrumentalness']
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            filename = file.filename
            filepath = os.path.join('static/uploads', filename)  # Path to save the uploaded file
            file.save(filepath)
            # Perform any addi<LeftMouse>tional processing on the uploaded file
            label = model_app(filepath)
            return render_template('home.html', filename=filename, output = label)
    return render_template('home.html',inputs = inputs,para = para)

@app.route('/open_track', methods=['POST'])
def open_track():
    track_id = open_spotify(arr)[14:]
    print(open_spotify(arr)[14:])
    track_url = f"https://open.spotify.com/track/{track_id}"
    return redirect(track_url)
    
    
@app.route('/process', methods=['POST'])
def process_form():
    global arr
    value = dict()
    inputs = ['valence', 'danceability', 'duration (ms)', 'loudness', 'spec_rate', 'liveness', 'energy', 'speechiness', 'tempo', 'acousticness', 'instrumentalness']
    for i in inputs:
    	value[i] = request.form.get('valence')
    arr,label = predict(value)
    para = f"The model has classified the song as {label}"
    return render_template('home.html',para = para,label = label)

@app.route('/about')
def about():
     return render_template('about.html')
