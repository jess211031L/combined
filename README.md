# MLOPS by jess, philander ,ryan
---

# Combined Project

This project is a demonstration of an MLOps workflow, combining multiple machine learning models and web applications into a single deployment. The project showcases how to manage different aspects of an ML project, from development and configuration management to deployment.

## Project Overview

This repository contains a combined application that integrates two main components:

1. **Mushroom Classification App**: A web application that predicts the class of mushrooms based on various input features.
2. **Transaction Anomaly Detection App**: A web application for anomaly detection in financial transactions.

## Project Structure

The repository is organized as follows:

```
combined/
│
├── data/                         # Folder containing datasets used in the project
│   ├── dataset1.csv
│   └── dataset2.csv
│
├── models/                       # Folder containing trained machine learning models
│   └── mushroom_classification_model.pkl
│
├── templates/                    # HTML templates for the web applications
│   ├── fillbird.html
│   ├── jess.html
│
├── combined_app.py               # Combined application integrating both apps
├── dataset2_jess.ipynb           # Jupyter notebook for the second dataset analysis
├── dataset3_philander.ipynb      # Jupyter notebook for the third dataset analysis
├── fillbird_app.py               # Original Transaction Anomaly Detection application code
├── jess_app.py                   # Original Mushroom Classification application code
├── requirements.txt              # List of dependencies needed to run the project
└── README.md                     # This README file
```

## How to Run the Application

### Prerequisites

- Python 3.11
- Git
- Pip
- Anaconda (optional but recommended)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/jess211031L/combined.git
    cd combined
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Initialize and set up the environment:

    ```bash
    conda create -n myenv python=3.11
    conda activate myenv
    ```

### Running the Application

1. **Mushroom Classification App**:

    - Navigate to the root directory of the project.
    - Run the application:

    ```bash
    python combined_app.py
    ```

2. **Fillbird App**:

    - The same combined app handles both the mushroom classification and the transaction anomaly detection.
    - You can access the respective apps by navigating to the appropriate URLs on your localhost.

### Deployment

- The application is deployed to a cloud platform such by Render.
- Use the command below for deployment using Gunicorn:

    ```bash
    gunicorn combined_app:app
    ```

## Features

- **Mushroom Classification**: Predict the edibility of mushrooms based on features like cap shape, cap surface, bruises, etc.
- **Anomaly Detection**: Detect anomalies in financial transactions.


## Authors

- Jess - Developer and Project Lead
- Philander - Contributor
- Ryan - Contributor



