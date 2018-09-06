import logging


logging.basicConfig(format='%(levelname)s:\033[34m %(message)s\033[0m',level=logging.DEBUG)

logging.debug('this is a debug message')
logging.info('this is a info message')
logging.warn('this is a warn message')
logging.error('this is a warn message')
