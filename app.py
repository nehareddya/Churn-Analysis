import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model_LR.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    if prediction == [0]:
        return render_template('index.html',prediction_text = 'The Customer should not churn')
    elif prediction == [1]:       
        return render_template('index.html',prediction_text = 'The Customer should churn')  
    
if __name__ == "__main__":
    app.run(debug=True)
