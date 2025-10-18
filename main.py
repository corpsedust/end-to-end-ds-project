#temporary fix , without which code from line 5 throws error ds_project
#not found
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))


#logging functionality is added because when app deployed on cloud
#you do not have terminal, so you need this 
from ds_project import logger
logger.info("Welcome to our custom logging")

