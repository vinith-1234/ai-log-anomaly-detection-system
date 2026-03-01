from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(contamination=0.2)

def train_model():
    data = np.array([
        [1,0,0,5],
        [2,1,0,6],
        [0,0,0,3],
        [1,1,0,4],
        [10,5,2,20]
    ])
    model.fit(data)

train_model()

def predict(features):
    result = model.predict([features])[0]
    score = model.decision_function([features])[0]
    return result, score