# Kidney-Disease-Classification (MLOps-Based) — MLflow & DVC

## 🌟 Workflows Overview

Workflows in this project simplify kidney disease classification by organizing tasks into clear, actionable steps. They ensure reproducibility, traceability, and efficient deployment, following MLOps best practices# Project: Kidney Disease Prediction

## Directory Structure

```plaintext
singhsourav0-kidney-disease/
├── README.md
├── LICENSE
├── dvc.yaml
├── init_setup.sh
├── main.py
├── params.yaml
├── pyproject.toml
├── requirements.txt
├── requirements_dev.txt
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
│   ├── kidney-CT-Scan-data.zip
│   └── trials.ipynb
├── src/
│   └── CNNclassifier/
│       ├── __init__.py
│       ├── __pycache__/
│       ├── components/
│       │   ├── __init__.py
│       │   ├── data_ingestion.py
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
│       │   └── stage_02_prepare_base_model.py
│       └── utils/
│           ├── __init__.py
│           └── common.py
├── tests/
│   ├── __init__.py
│   ├── integration/
│   │   └── __init__.py
│   └── unit/
│       └── __init__.py
└── .github/
    └── workflows/
        └── .gitkeep
```



## 📊 Workflows

1. ✅ Update `config.yaml`
2. 🔐 Update `secrets.yaml` [Optional]
3. ⚙️ Update `params.yaml`
4. 🗄 Update the entity
5. 🔧 Update the configuration manager in `src/config`
6. ➕ Update the components
7. ➖ Update the pipeline
8. 🔄 Update `main.py`
9. 🕒 Update `dvc.yaml`
10. 🚀 Update `app.py`

---

## 🔢 How to Run?

### ✍️ Steps:

1. **Clone the repository**
   ```bash
   git clone https://github.com/singhsourav0/Kidney-Disease.git
   ```
2. **Create a Conda environment**
   ```bash
   conda create -n cnncls python=3.8 -y
   conda activate cnncls
   ```
3. **Install the requirements**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**
   ```bash
   python app.py
   ```
5. **Access the application**
   ```bash
   Open your localhost and port.
   ```

---

## 🕹️ MLflow

- [🔗 Documentation](https://mlflow.org/docs/latest/index.html)
- [🎥 MLflow Tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

MLflow manages the ML lifecycle, providing tools for experiment tracking, model management, and deployment. Its integration with DVC and AWS ensures consistency and scalability. It’s pivotal in tracking experiments and managing models efficiently.

### Commands:

- Start MLflow UI:
  ```bash
  mlflow ui
  ```
- DagsHub Integration:
  ```bash
  export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/Kidney-Disease-Classification-MLflow-DVC.mlflow
  export MLFLOW_TRACKING_USERNAME=entbappy
  export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0
  python script.py
  ```

---

## 🎨 DVC Commands

1. Initialize DVC:
   ```bash
   dvc init
   ```
2. Reproduce pipeline:
   ```bash
   dvc repro
   ```
   **Use Case:** Automatically detects and executes necessary steps when data or pipeline changes, ensuring up-to-date results.

3. Visualize DAG:
   ```bash
   dvc dag
   ```
   **Use Case:** Provides a clear pipeline overview, aiding team collaboration and understanding of data dependencies.

---

## 🌍 About MLflow & DVC

### MLflow and DVC: A Collaborative Framework

The synergy between MLflow and DVC in this project creates a powerful framework for managing machine learning workflows. While MLflow excels at tracking experiments, managing model versions, and facilitating deployments, DVC complements it by orchestrating data versioning and pipeline reproducibility. This combination ensures that every aspect of the ML lifecycle—from data preparation to model deployment—is both traceable and reproducible, addressing key challenges in MLOps.

### MLflow

- 🔧 **Production Grade**
- 📋 Tracks all your experiments
- ✍️ Logs and tags your models

### DVC

- 💡 **Lightweight for POC**
- 🌀 Tracks lightweight experiments
- 🔄 Performs orchestration (e.g., creating pipelines)

---

## 🌐 AWS-CI/CD Deployment with GitHub Actions

### ✅ Steps:

1. **Login to AWS Console**

2. **Create IAM User**
   - Permissions:
     - EC2 for VM management
     - ECR for Docker image storage

3. **Set Up ECR Repository**
   - Example URI:
     ```
     566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken
     ```

4. **Create EC2 Instance**
   - Install Docker:
     ```bash
     curl -fsSL https://get.docker.com -o get-docker.sh
     sudo sh get-docker.sh
     sudo usermod -aG docker ubuntu
     newgrp docker
     ```

5. **Configure EC2 as a Runner**
   - Instructions available under `Settings > Actions > Runner > New Self-Hosted Runner`.

6. **Set GitHub Secrets**
   - Required keys:
     ```
     AWS_ACCESS_KEY_ID=
     AWS_SECRET_ACCESS_KEY=
     AWS_REGION=us-east-1
     AWS_ECR_LOGIN_URI=566373416292.dkr.ecr.ap-south-1.amazonaws.com
     ECR_REPOSITORY_NAME=simple-app
     ```

---

### 🌐 Summary

This project integrates MLflow for tracking, DVC for orchestration, and AWS CI/CD for deployment, creating a scalable, maintainable pipeline for kidney disease classification. These tools ensure reproducibility, automation, and robust deployment practices, making it ready for production use.

