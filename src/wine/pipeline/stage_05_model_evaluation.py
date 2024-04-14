from wine.config.configuration import ConfigurationManager
from wine.components.model_evaluation import ModelEvaluation
from wine import logger


STAGE_NAME = "MODEL EVALUATION"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> starting {STAGE_NAME} stage <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> completed {STAGE_NAME} stage <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e