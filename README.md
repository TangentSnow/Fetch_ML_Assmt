# Fetch_ML_Assessment
Given the number of the observed scanned receipts each day for the year 2021, an algorithm which can predict the approximate number of the scanned receipts for each month of 2022.

## Description
Utilizing a Neural Network consisting of just two layers, predicting the approximate number of the scanned receipts for a user entered month in 2022.
The user is prompted to a simple web page that is hosted locally using the Flask API, they can enter a month in 2022 and get a prediction.

## Getting Started
In a command-line run:
    `git pull`
    and cd into the project directory

### Run using Docker Hub Image
In the command-line run the following commands:<br>
    `docker pull adityamakineni/fetch_ml_assmt:latest` //pulls and loads the docker image from docker hub<br>
    `docker run -d -p 3000:3000 adityamakineni/fetch_ml_assmt:latest` //runs the docker container on port 3000<br>
    Open a browser and entwer the URL:`localhost:3000`<br>
    To stop container: `docker container stop (unique code generated)`<br>

### Run using Dockerfile
**Make sure the Docker application is running in the background**
In the command-line run the following commands:<br>
    `docker build -t adityamakineni/fetch_ml_assmt .` //Builds the docker image from docker file<br>
    `docker run -d -p 3000:3000 adityamakineni/fetch_ml_assmt` //Runs image on port 3000
    Open a browser and entwer the URL:`localhost:3000`<br>
    To stop container: `docker container stop (unique code generated)`<br>


### Run using predictor.py
In the command-line run the following:
    `pip install -r requirements.txt` //downloads the necessary packages<br>
    `python predictor.py`<br> 
    Copy the link and paste it into a browser<br>
