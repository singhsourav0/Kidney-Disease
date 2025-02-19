import os
import mlflow

# Set MLflow environment variables
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/darkathon89/Kidney-Disease.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "darkathon89"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "9c6a621ab46434d5e99ba9b0be13ae5e31c233dd"

# Verify MLflow tracking URI
print("MLflow Tracking URI:", mlflow.get_tracking_uri())
