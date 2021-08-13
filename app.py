#import libraries
from flask import Flask, render_template, request
from transform_for_prediction import *
import pickle

#create an instance
app = Flask(__name__)

#load SVR model
model = pickle.load(open('support_vector_regression_model.pkl', 'rb'))

#tell flask what URL should trigger the function and what action to perform with GET request (loads home page)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

#tell flask what URL should trigger the function with POST request (posts prediction)
@app.route("/predict", methods=['POST'])

def predict():
    
    #if request is post
    if request.method == 'POST':
        
        #gather user input
        name = request.form['cn']
        year = int(request.form['yr'])
        avg_price = float(request.form['avg_price'])/10000
        kilometers = float(request.form['milage'])*1.60934
        fuel = str(request.form['fuel'])
        seller = str(request.form['seller'])
        transmission = str(request.form['trans'])
        owners = int(request.form['owner'])
        
        #replaces underscores with spaces
        name = name.replace("_", " ")
        
        #sends user input to be transformed into usable form by model
        transform = transform_for_prediction(name,year,avg_price,kilometers,fuel,seller,transmission,owners)
        
        #make a prediction using SVR pickle
        prediction = model.predict(transform)
        
        #put output in proper form
        output = round(prediction[0],2)*10000
        
        #display output
        return render_template('index.html', prediction_text = "Predicted Sale Price (USD): {}".format(output))
    
    #if request isn't post
    else:
        
        return render_template('index.html')

#if flask instance is __main__ then debug
if __name__ == "__main__":
    
    app.run(debug=True)

