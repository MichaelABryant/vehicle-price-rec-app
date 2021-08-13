# Vehicle Sales Price Prediction App (Python/HTML)

This repository is for hosting the files used to build the [Heroku web app](https://predict-vehicle-price.herokuapp.com/) based on [the analysis and models built on a vehicle sales dataset](https://github.com/MichaelBryantDS/vehicle-price-pred). Below you will find an overview of the code and files.

### Code Used 

**Python Version:** 3.8.11 <br />
**Packages:** pandas, numpy, scipy, sklearn, flask, pickle<br />
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  

## Files

### templates/index.html

This file contains the HTML code used for the front end of the app hosted with Heroku.

### Procfile

This file contains the commands for running the application's containers. It specifies the application server as Gunicorn.

### app.py

This file contains the flask actions and input manipulation performed for the application.

### scaler.pkl

This file is the pickle containing the MinMaxScaler after it had been fit to the training data so that it can transform the user input.

### support_vector_regression_model.pkl

This file is the pickle containing the hyperparameter tuned SVR after being trained on the training data so that it can be applied to the user input.

### transform_for_prediction.py

This file contains a function used in the app.py file to process the user input (i.e., create dummy variables and scale) so that the model can make a prediction.

## Future work

## Resources

1. [Kaggle: Vehicle dataset](https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho)
2. [YouTube: Live- Implementation of End To End Kaggle Machine Learning Project With Deployment by Krish Naik](https://www.youtube.com/watch?v=p_tpQSY1aTs)


