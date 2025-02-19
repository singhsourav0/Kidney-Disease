

import os
import sys

# Ensure Python can find the 'src' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from src.CNNclassifier.config.configuration import ConfigurationManager
from src.CNNclassifier.components.prepare_model import PrepareBaseModel
from src.CNNclassifier import logger

STAGE_NAME = "Prepare Base Model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        logger.info(f"{STAGE_NAME} started")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e
