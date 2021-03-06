from datetime import datetime
import logging

logging.basicConfig(filename="Milestone1B_Log.txt", format='%(message)s',filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
def log(message):
    logger.info(f'{datetime.now()};{message}')
