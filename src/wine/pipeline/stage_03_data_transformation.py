from wine.config.configuration import ConfigurationManager
from wine.components.data_transformation import DataTransformation
from wine import logger
from pathlib import Path


STAGE_NAME = "DATA TRANSFORMATION"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()

            else:
                raise Exception("Invalid data schema")

        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> starting {STAGE_NAME} stage <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> completed {STAGE_NAME} stage <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e