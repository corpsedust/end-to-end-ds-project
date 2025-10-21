from ds_project.config.configuration import ConfigurationManager
from ds_project.components.data_validaton import DataValidation
from ds_project import logger

STAGE_NAME = "Data Validation stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config = data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
            
            
            
if __name__ == "__main__":
    try:
        logger.info(f">>> stage {STAGE_NAME} started <<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e