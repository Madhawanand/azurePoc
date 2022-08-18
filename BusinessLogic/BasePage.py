import inspect
import logging
import os.path
from datetime import datetime

import pytest
import os


class BaseTest:

    def getLogger(self):
        # workingDir = os.getcwd()
        # print(workingDir)
        #  os.chdir('../../Reports')
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        current_datetime = datetime.now()
        print("Current date & time : ", current_datetime)

        # convert datetime obj to string
        str_current_datetime = str(current_datetime)

        # create a file object along with extension
        file_name = str_current_datetime + ".log"
        fileHandler = logging.FileHandler(file_name)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
