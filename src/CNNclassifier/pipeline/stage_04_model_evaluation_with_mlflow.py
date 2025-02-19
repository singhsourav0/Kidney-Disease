import os
import sys  # This ensures the environment is set before MLflow runs

import mlflow
print("Using MLflow Tracking URI:", mlflow.get_tracking_uri())

# Your MLflow experiment and logging code

# Ensure Python can find the 'src' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from src import mlflow_setup
from src.CNNclassifier.config.configuration import ConfigurationManager
from src.CNNclassifier.components.model_evaluation_mlflow import Evaluation
from src.CNNclassifier import logger


STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()
        evaluation.save_score()



if __name__ == '__main__':
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = EvaluationPipeline()
            obj.main()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e