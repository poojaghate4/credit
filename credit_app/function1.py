import pickle
import config1

model = pickle.load(open(config1.MODEL_PATH,'rb'))


def credit_prediction(data):

    result = model.predict(data)
    

    if result[0] == 1:
        return "Credit Card Approved"

    else:
        return  "Credit Card Not Approved"
