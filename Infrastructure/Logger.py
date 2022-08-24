import logging

#wraps native logging
class Logger():
    def __init__(self):
        #could be used for intializing a self contained logger
        pass

    def info(self, message):
        logging.info(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)
