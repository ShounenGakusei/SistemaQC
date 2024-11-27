import logging
from utils.config import Config


def setup_logging():
    # Configuración de logs
    log_level = Config.LOG_LEVEL
    log_file = Config.LOG_FILE

    logging.basicConfig(level=log_level,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler(log_file),
                            logging.StreamHandler()
                        ])
