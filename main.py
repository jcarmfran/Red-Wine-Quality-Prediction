from wine import logger
from wine.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from wine.pipeline.stage_02_data_validation import DataValidation
# from wine.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from wine.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from wine.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidation()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e