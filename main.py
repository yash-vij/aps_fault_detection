from sensor.logger import logging
from sensor.execption import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os
from sensor.entity import config_entity
from sensor.components.DataIngestion import DataIngestion



if __name__ == "__main__":
     try:
          #test_logger_and_exception()

          #get_collection_as_dataframe(database_name="aps_test",collection_name="sensor_test")

          training_pipeline_config = config_entity.TrainingPipelineConfig()

          #data_ingestion
          data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
          data_ingestion_artifact = data_ingestion.initiate_data_ingestion()


     except Exception as e:
          print(e)
