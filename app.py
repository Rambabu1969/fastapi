
# 1. Library imports
import uvicorn
from fastapi import FastAPI
import pickle

# 2. Create the app object
app = FastAPI()

# 3. load the model
model = pickle.load(open("rf.pkl", "rb"))

# 4. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get("/predict")
def getUserInfo(TimeTaken: int, CorrectAnswers: int):
    prediction = model.predict([[TimeTaken,CorrectAnswers]])
    if(prediction[0]>0.5):
        prediction="Malpractice"
    else:
        prediction="Normal"
    return {
        'prediction': prediction
    }


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
    
#uvicorn app:app --reload
