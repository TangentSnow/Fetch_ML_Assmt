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
In the command-line run the following commands:\n
    ```
    docker pull adityamakineni/fetch_ml_assmt:latest //pulls and loads the docker image from docker hub
    docker run -d -p 3000:3000 adityamakineni/fetch_ml_assmt:latest //runs the docker container on port 3000
    Open a browser and entwer the URL:localhost:3000
    To stop container: `docker container stop (unique code generated)
    ```

### Run using predictor.py
In the command-line run the following:
    `pip install -r requirements.txt` //downloads the necessary packages
    `python predictor.py` 
    Copy the link and paste it into a browser
