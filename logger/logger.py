#create logger class to log messages to a file
import logging

class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        handler = logging.FileHandler("app.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def info(self, message: str):
        self.logger.info(message)

    def error(self, message: str):
        self.logger.error(message)
        
    def debug(self, message: str):
        self.logger.debug(message)
