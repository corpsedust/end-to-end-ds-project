from ds_project import logger
from ds_project.pipeline.stage01_data_ingestion import DataIngestionTrainigPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = DataIngestionTrainigPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e