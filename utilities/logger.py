import inspect
import logging
from pathlib import Path


class Utilities:
    ROOT_DIR = Path(__file__).resolve().parent.parent
    def custom_logger(self, logLevel=logging.INFO):
        # Set class/method name from where its called
        logger_name = inspect.stack()[1][3]

        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        # create console handler or file handler and set the log level
        fh = logging.FileHandler(self.ROOT_DIR/'log'/'automation.log')
        ch = logging.StreamHandler()

        # create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s')

        # add formatter to console or file handler
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(fh)
        logger.addHandler(ch)

        return logger