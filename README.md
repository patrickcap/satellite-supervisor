# Satellite Purpose Prediction

![Satellite](/assets/images/nasa-8Hjx3GNZYeA-unsplash.jpg)
*A satellite orbiting above the ocean. Credit: [unsplash.com](https://unsplash.com/photos/satellite-flying-on-space-8Hjx3GNZYeA)*

## Overview

This repository contains code for predicting the purpose of a satellite based on limited information. The purpose prediction is performed using machine learning techniques applied to satellite data.

## Purpose

The main purpose of this project is to demonstrate the application of machine learning algorithms in predicting the purpose of satellites based on a limited set of features. The prediction model aims to classify the purpose of a satellite into predefined categories using the provided data.

## Features

- **Limited Information**: Predictions are made using only a subset of features available for each satellite.
- **Machine Learning**: Various machine learning algorithms are explored and evaluated for their effectiveness in predicting satellite purposes.
- **Data Preprocessing**: Data preprocessing techniques are applied to prepare the input data for model training.
- **Model Evaluation**: The performance of different models is evaluated using appropriate metrics to assess their accuracy and reliability.

## Prerequisites
- Ensure that your 8080 port is available, if not, make it available by terminating processes occupying it or change the source code of the repository to use a different port.

## Getting Started

To get started with using the prediction model:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/satellite-purpose-prediction.git

2. Install the required dependencies
    ```bash
    pip install -r requirements.txt

3. Launch the API
    ```bash
    cd scripts/
    ./launch_api.sh

4. Click on the link provided in the terminal and authenticate your use of the API using the key also provided in the terminal.

