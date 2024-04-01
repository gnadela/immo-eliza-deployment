# Immo Eliza Prediction Model Deployment Project
## Introduction

This project aims to deploy a machine learning model for predicting real estate property prices in Belgium for the real estate company Immo Eliza. This project is a continuation of [Immo Eliza Machine Learning Model Development Project](https://github.com/gnadela/immo-eliza-ml/blob/main/README.md)


## Repo Structure
```
immo-eliza-deployment/
│
├── api/
│   ├── app.py
│   ├── predict.py
│   └── trained_model.pkl
├── streamlit
│   └── streamlit_app.py
├── Dockerfile
├── README.md
└── requirements.txt
```


## Data

This deployment pulls the model from [Immo Eliza Machine Learning Model Development Project](https://github.com/gnadela/immo-eliza-ml/blob/main/README.md) that has been stored using Pickle. 


## Model DeDeployment

In this deployment, an API is created using FastAPI, placed in a Docker container, and made viewable via Streamlit.





## Usage

Clone the repository:

```
git clone https://github.com/gnadela/immo-eliza-deployment
cd immo-eliza-deployment
```

Install dependencies:
```
pip install -r requirements.txt
```
### FastAPI
Run FastAPI:
```
cd api
python app.py 
uvicorn app:app --reload
```
The API can now be accessed from:
```
http://127.0.0.1:8000/
```
### Docker

Alternatively, you can run FastAPI from a Docker container.
```
docker build -t fastapi-app .
docker run -d -p 8080:80 fastapi-app
```
### Streamlit
To run Streamlit:
```
cd streamlit
streamlit run streamlit_app.py
```
This is the result:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.116:8501
```
 Some pre-filled information have been provided for ease of testing.  

 ### Streamlit Community

 The Streamlit app is deployed at:
`
 https://immo-eliza-deployment-gnadela.streamlit.app/
`
However, the site currently fails in rendering the prediction. To be continued....


## Timeline
This project took 1 week for completion.

## Personal Situation

This project was done as part of the AI Bootcamp at BeCode.org. This is my first machine learning model deployment project.

Connect with me on [LinkedIn](https://www.linkedin.com/in/geraldine-nadela-60827a11/).