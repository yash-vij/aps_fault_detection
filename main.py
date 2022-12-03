import sys

from sensor.logger import logging
from sensor.execption import SensorException
from sensor.utils import get_collection_as_dataframe

def test_logger_and_exception():
     try:
          logging.info("Stopping the test_logger_and_exception")
          result = 3/0
          print(result)
          logging.info("Stopping the test_logger_and_exception")
     except Exception as e :
          logging.debug(str(e))

          raise SensorException(e, sys)


if __name__ == "__main__":
     try:
          #test_logger_and_exception()
          get_collection_as_dataframe("aps_test","sensor_test")
     except Exception as e:
          print(e)
