import logging 
logger =logging.getLogger(__name__)
def print_hello():
    print("hello")
    logger.info("called cronjob")