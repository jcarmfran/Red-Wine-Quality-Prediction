from wine import logger
from wine.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from wine.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from wine.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from wine.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from wine.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "DATA INGESTION"
try:
    logger.info(f">>>>>> starting {STAGE_NAME} stage <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> completed {STAGE_NAME} stage <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "DATA VALIDATION"
try:
    logger.info(f">>>>>> starting {STAGE_NAME} stage <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> completed {STAGE_NAME} stage <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "DATA TRANSFORMATION"
try:
    logger.info(f">>>>>> starting {STAGE_NAME} stage <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> completed {STAGE_NAME} stage <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "MODEL TRAINING"
try:
    logger.info(f">>>>>> starting {STAGE_NAME} stage <<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> completed {STAGE_NAME} stage <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e