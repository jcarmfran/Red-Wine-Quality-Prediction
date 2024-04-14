from wine.config.configuration import ConfigurationManager
from wine.components.model_trainer import ModelTrainer
from wine import logger

STAGE_NAME = "MODEL TRAINING"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> starting {STAGE_NAME} stage <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> completed {STAGE_NAME} stage <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e