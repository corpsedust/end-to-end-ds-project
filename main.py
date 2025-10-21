from ds_project import logger
from ds_project.pipeline.stage01_data_ingestion import DataIngestionTrainigPipeline
from ds_project.pipeline.stage02_data_validaton import DataValidationTrainingPipeline


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


#why are we again using try, catch block here when we have 
#already defined the shit in stage02 under __name__ = "__main__"