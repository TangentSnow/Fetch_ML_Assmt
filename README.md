# Fetch_ML_Assessment
Given the number of the observed scanned receipts each day for the year 2021, this program can predict the approximate number of the scanned receipts for each month of 2022.<br>

## Description
Utilizing a Neural Network consisting of just two layers, predicting the approximate number of scanned receipts for a user entered month in 2022.<br>
The user is prompted to a simple web page that is hosted locally using Flask API, they can enter a month in 2022 and get a prediction.<br>

## Frameworks used
Pandas<br>
NumPy<br>
Matplotlib<br>
PyTorch<br>
Flask<br>

## Getting Started
### Clone project
```
git clone https://github.com/TangentSnow/Fetch_ML_Assmt.git
```

### Navigate into the project folder
```
cd Fetch_ML_Assmt
```

## Two ways to run:
**1) Using Docker <br>
2) Using python file**

### Run using Dockerfile:
This method requires Docker<br>
Download Docker at [https://www.docker.com/products/docker-desktop/]<br>
After installation, open docker to start the docker engine and leave it running in the background<br>

Build Docker Image from Dockerfile<br>
```
docker build -t adityamakineni/fetch_ml_assmt .
```

Run Image in a docker container on port 3000<br>
```
docker run -d -p 3000:3000 adityamakineni/fetch_ml_assmt
```

Open a browser and enter
```
localhost:3000
```

Get a prediction
```
Enter a month (ex: January, November...(no spaces)) into the text box and click predict
```

Stop container 
```
docker container stop <unique code generated>
```


### Run using python file
Download the required python packages
```
pip install -r requirements.txt
```
Run the python file
```
python predictor.py
```
You will get something like the following:
```
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:3000
 * Running on http://172.24.99.18:3000
```
You can copy either one of the http links and paste it into a browser to access the web page

Get a prediction
```
Enter a month (ex: January, November...(no spaces)) into the text box and click predict
```
Exit program
```
Press Control + C
```
