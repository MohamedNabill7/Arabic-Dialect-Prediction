from Utils import preprocess
from joblib import load
from flask import Flask, request, jsonify, render_template


model = load(r"C:\Users\Mohamed Nabil\Documents\AIM Task\Modeling\ML_dialect.joblib")

labels = {'SA':'Saudi Arabia','QA':'Qatar','KW':'Kuwait','OM':'Oman','AE':'Arab Emirates','BH':'Bahrain',
          'IQ':'Iraq','YE':'Yemen','EG':'Egypt','SD':'Sudan','SY':'Syria','JO':'Jordan',
          'PL':'Palestine','LB':'Lebanon','DZ':'Algeria','MA':'Morocco','TN':'Tunisia','LY':'Libya'}


# Initialize the app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('predictor.html')


@app.route('/predict', methods = ['POST'])
def predict():
    sentence = request.form['sentence']
    data = [preprocess(sentence)]
        
    if model.predict(data)[0] in labels.keys():
        pred = labels[model.predict(data)[0]]
        
    return render_template('predictor.html', 
                           answer = pred)

# Start the server, continuously listen to requests.
if __name__=="__main__":
    app.run(debug=False)
