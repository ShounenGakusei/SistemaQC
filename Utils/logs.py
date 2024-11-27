import logging
from utils.config import Config


import logging

def setup_logging():
    logger = logging.getLogger('SistemaQC')  # Nombre único para tu aplicación
    if not logger.hasHandlers():  # Evita duplicados
        # Configuración de logs
        log_level = Config.LOG_LEVEL
        log_file = Config.LOG_FILE

        logging.basicConfig(level=log_level,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            handlers=[
                                logging.FileHandler(log_file),
                                logging.StreamHandler()
                            ])

    return logger

# Configura el logger al importar este módulo
logger_qc = setup_logging()

