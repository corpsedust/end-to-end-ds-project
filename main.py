from ds_project import logger
from ds_project.pipeline.stage01_data_ingestion import DataIngestionTrainigPipeline
from ds_project.pipeline.stage02_data_validaton import DataValidationTrainingPipeline
from ds_project.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from ds_project.pipeline.stage04_modeltraining import ModelTrainerTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = DataIngestionTrainigPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.excetpion(e)
    raise e

#why are we again using try, catch block here when we have 
#already defined the shit in stage02 under __name__ = "__main__"