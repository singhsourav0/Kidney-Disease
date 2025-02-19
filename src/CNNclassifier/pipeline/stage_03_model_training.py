import os
import sys

# Ensure Python can find the 'src' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.CNNclassifier.config.configuration import ConfigurationManager
from src.CNNclassifier.components.model_training import Training
from src.CNNclassifier import logger

STAGE_NAME = "Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()



if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        
    