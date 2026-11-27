
import joblib
import os

# Check whether model file exists
model_file = "iris_model.pkl"

if os.path.exists(model_file):

    # Load saved model
    model = joblib.load(model_file)

    print("MACHINE LEARNING MODEL LOADING")
    print("------------------------------")
    print("Model file:", model_file)
    print("Model loaded successfully!")

    print("Model Type:", type(model).__name__)
    print("Number of Trees:", model.n_estimators)

else:
    print("Model file not found!")

