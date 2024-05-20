import logging

baseloader_logger = logging.getLogger('baseloader')
baseloader_logger.setLevel(logging.DEBUG)  
coinbaseloader_logger = logging.getLogger('coinbaseloader')
coinbaseloader_logger.setLevel(logging.DEBUG)  

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

baseloader_logger.addHandler(file_handler)
coinbaseloader_logger.addHandler(file_handler)

baseloader_logger.setLevel(logging.INFO)

class CustomFormatter(logging.Formatter):
    def format(self, record):
        formatted_message = super().format(record)
        return f'[CUSTOM] {formatted_message}'

custom_formatter = CustomFormatter()
file_handler.setFormatter(custom_formatter)