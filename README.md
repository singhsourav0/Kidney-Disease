# 🏥 Kidney Disease Classification using CNN

## 📌 Project Overview

This project focuses on detecting **kidney disease** from medical images using a **Convolutional Neural Network (CNN)**. The pipeline integrates **MLflow** for experiment tracking and **DVC (Data Version Control)** for dataset management.

## 🚀 Features

- **Data Ingestion** 📥: Load and preprocess medical images.
- **Model Training** 🎯: Train a deep learning model using CNN.
- **MLflow Tracking** 📊: Log experiments and monitor performance.
- **Model Evaluation** ✅: Assess performance using various metrics.
- **DVC Integration** 📂: Manage dataset versions effectively.

## 💽 Project Structure

```
└── singhsourav0-kidney-disease/
    ├── README.md
    ├── LICENSE
    ├── dvc.lock
    ├── dvc.yaml
    ├── init_setup.sh
    ├── main.py
    ├── params.yaml
    ├── pyproject.toml
    ├── requirements.txt
    ├── requirements_dev.txt
    ├── scores.json
    ├── setup.cfg
    ├── setup.py
    ├── templates.py
    ├── tox.ini
    ├── configs/
    │   └── config.yaml
    ├── logs/
    ├── research/
    │   ├── 01_data_ingestion.ipynb
    │   ├── 02_prepare_base_model.ipynb
    │   ├── 03_model_training.ipynb
    │   ├── 04_model_evaluation.ipynb
    │   ├── kidney-CT-Scan-data.zip
    │   └── trials.ipynb
    ├── src/
    │   ├── __init__.py
    │   ├── mlflow_setup.py
    │   └── CNNclassifier/
    │       ├── __init__.py
    │       ├── components/
    │       │   ├── __init__.py
    │       │   ├── data_ingestion.py
    │       │   ├── model_evaluation_mlflow.py
    │       │   ├── model_training.py
    │       │   └── prepare_model.py
    │       ├── config/
    │       │   ├── __init__.py
    │       │   └── configuration.py
    │       ├── constants/
    │       │   └── __init__.py
    │       ├── entity/
    │       │   ├── __init__.py
    │       │   └── config_entity.py
    │       ├── pipeline/
    │       │   ├── __init__.py
    │       │   ├── stage_01_data_ingestion.py
    │       │   ├── stage_02_prepare_base_model.py
    │       │   ├── stage_03_model_training.py
    │       │   ├── stage_04_model_evaluation_with_mlflow.py
    │       └── utils/
    │           ├── __init__.py
    │           └── common.py
    ├── tests/
    │   ├── __init__.py
    │   ├── integration/
    │   │   └── __init__.py
    │   └── unit/
    │       └── __init__.py
    ├── .github/
    │   └── workflows/
```

## 🔁 Workflow Diagram

```
+----------------+            +--------------------+
| data_ingestion |            | prepare_base_model |
+----------------+            +--------------------+
      **             **              **             **
    **                 ***        ***                 **
  **                      **    **                      **
***                     +----------+                     ***
   *****                | training |                *****
        *****           +----------+           *****
             *****            *           *****
                  *****       *      *****
                       ***    *   ***
                      +------------+
                      | evaluation |
                      +------------+
```

## 🔗 DVC & MLflow Links

- 📂 **DVC Repository**: [Kidney Disease DVC](https://dagshub.com/darkathon89/Kidney-Disease)
- 📊 **MLflow Tracking**: [Kidney Disease MLflow](https://dagshub.com/darkathon89/Kidney-Disease.mlflow)

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

## 🎯 Running the Project

To run the model:
```bash
python app.py
```

To run or retrain the model:
```bash
python main.py
```

Alternatively, you can use DVC to reproduce the pipeline:
```bash
dvc repro
```

## 🤝 Contributing

Feel free to open issues or pull requests! 🚀

