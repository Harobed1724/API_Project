# Sepsis Prediction FastAPI API

## Overview

This repository contains a FastAPI API for predicting sepsis based on a machine learning model. The model is built using scikit-learn and is available as a joblib pipeline. The API accepts input data related to various health parameters and returns a prediction regarding the likelihood of sepsis.


## FAST API and Docker
### What is FastAPI?
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed to be easy to use and to provide automatic interactive documentation (using Swagger UI and ReDoc) while also being fast to execute. FastAPI is built on top of Starlette and Pydantic, leveraging their capabilities for asynchronous programming and data validation, respectively.


### What is Docker?
Docker is a platform designed to make it easier to create, deploy, and run applications using containers. Containers allow developers to package an application and its dependencies into a single, lightweight unit that can run consistently across various environments. Docker provides a set of tools and a platform for managing these containers.


For this project, datasets provided on [Kaggle] was used. Below are steps followed to create an API and dockerize it.

#### 1. Load and Analyze Data:

* Load the train and test datasets.

* Analyze and preprocess the data.

* Explore the distribution of features and the target variable.

#### 2. Train a Machine Learning Model:

* Split the dataset into features (X) and target (y).

* Balance the dataset 

* Create pipeline 

* Train a machine learning models on the training data.For this project K-Near Neighbours, Decision tree,and Logistic Regression were used. 

#### 3. Save the Model:

* After training the model, save it using joblib so that it can be loaded later for predictions.


#### 4. Create FastAPI Application:

* Define the FastAPI application.

* Define a Pydantic model for the input data (InputData).

* Create an endpoint for prediction (predict).

#### 5. Make Predictions with the Model:

In the predict endpoint, input datails received, preprocessed, and the pre-trained model used for predictions.

#### 6. Dockerize the Application:

* Write a Dockerfile to containerize your FastAPI application.

* Build the Docker image.

* Run the Docker container.


## Setup


1. Clone the repository:

    ```bash
    git clone https://github.com/Harobed1724/API_Project.git
    cd your-repository
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI Server:
    ```bash
    uvicorn main:app --reload
    ```



## Endpoints
### Home Endpoint
http://0.0.0.0:8000/docs
Provides a welcome message for the Sepsis Prediction App API.

### Prediction Endpoint
http://0.0.0.0:8000/predict
Accepts POST requests with input data for sepsis prediction. Returns the prediction result.

### API after Dockerization
http://127.0.0.1:8000 

## Input Data Format
The input data for the prediction endpoint should be sent as a POST request in the JSON format with the following structure:
```bash
  {
  "Plasma_glucose": int,
  "Blood_work1": int,
  "Blood_Pressure": int,
  "Blood_work2": int,
  "Blood_work3": int,
  "BMI": float,
  "Blood_work4": float,
  "Age": int,
  "Insurance": int
}
```

## Response Format
The prediction endpoint will return a JSON response with the predicted result:
```bash
    {
  "prediction": "Positive"
}
```

## Note:

1. Make sure to have Python installed.
Ensure that FastAPI and other dependencies are installed using the provided requirements.txt file.

2. When you run an application from a Docker container, the application becomes accessible on the specified port of the host machine due to the port mapping. This allows you to interact with the application as if it were running directly on the host.

## Acknowledgements
We would like to thank Azubi Africa for the opportunity to learn how to build an API with FastAPI and furthur dockerize it. The experience has been amazing.

