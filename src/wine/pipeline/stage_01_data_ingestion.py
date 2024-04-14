from wine.config.configuration import ConfigurationManager
from wine.components.data_ingestion import DataIngestion
from wine import logger


STAGE_NAME = "DATA INGESTION"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> starting {STAGE_NAME} stage <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> completed {STAGE_NAME} stage <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e