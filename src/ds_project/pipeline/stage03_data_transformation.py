from ds_project.config.configuration import ConfigurationManager
from ds_project.components.data_transformation import DataTransormation
from ds_project import logger

STAGE_NAME = "Data Transformation stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt")) as f:
                status = f.read().split(" ")[-1]                                   #transformation stage is only executed if validation is true  
                
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransormation(config = data_transformation_config)
                data_transformation.train_test_splitting()

            else:
                raise Exception("Your data schema is not valid")
            
        except Exception as e:
            print(e)
            

if __name__ == "__main__":
        try:
            logger.info(f">>> stage {STAGE_NAME} started <<<")
            obj = DataTransformationTrainingPipeline()
            obj.main()
            logger.info(f">>> stage {STAGE_NAME} completed <<<<")
        except Exception as e:
            logger.exception(e)
            raise e