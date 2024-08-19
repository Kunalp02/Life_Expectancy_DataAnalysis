# Data Analysis

This repository contains a Python script for analyzing and preprocessing the Life Expectancy Data. The script handles missing values, removes duplicates, and encodes categorical variables to prepare the dataset for further analysis or machine learning tasks.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Required Python Libraries](#required-python-libraries)
- [Dataset](#dataset)
- [Running the Script](#running-the-script)
- [Key Functionalities](#key-functionalities)
- [Notes](#notes)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Prerequisites

Before running the script, ensure you have the following software installed:

- Python 3.x
- pip (Python package installer)

## Working

We have taken Life Expectancy Dataset from kaggle. In the 'preprocess.py' file we are preprocessing the dataset. the processed data saved by the file name Output.csv.
the same data is sent to the express js endpoint created in the server.js. as per the things stated in the assignemnt we have completed the setup and integration part.

## Steps to run


The script requires several Python libraries. You can install them using the following command:

```bash
pip install pandas numpy seaborn matplotlib scikit-learn

```
Below commands will initiate the npm project in the current dir and installs all the required packages.
```bash
npm init -y
npm install express body-parser

```

Now, to execute first run the preprocess.py file that file will processed the life expectancy dataset. It will save and generate the processed 'output.csv' dataset. that we will use as a processed data.

```bash

node server.js
```
this will start the server on 3000. in the server.js file we have specified the get and post endpoints. Get endpoint is responsible to render the received data on the '/api/data' and post method is responsible to receive the processed data from a python script.

Open another terminal and execute the 'scriptToSendData.py' file to send the processed data over the post endpoint.
```bash
python scriptToSendData.py
```

Now, we can see on the page we have received the procesed data.