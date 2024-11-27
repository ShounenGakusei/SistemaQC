import os

class Config:
    # Umbrales para la clasificación
    LOG_LEVEL = 'INFO'  # Nivel de logs: DEBUG, INFO, WARNING, ERROR
    LOG_FILE = 'app_logs.log'  # Archivo donde se guardan los logs
    MODEL_PATH = os.path.join(os.getcwd(), 'models', 'Model_02_CONV3D_clase_20240927_152142.hdf5')
    IMAGEM_PATH = os.path.join(os.getcwd(), 'imagenes')
    STATION_PATH = os.path.join(os.getcwd(), 'static', 'stations_data.csv')
    SAVE_IMAGES = True
    CANALES = ["07", "08", "13"]
    TIEMPOS = ["00", "50", "40", "30", "20", "10"]
    
    PORT = 5000
    MIN_IMAGE_SIZE = 20  * 1024 # 20 MB
    MAX_TEMP_FOLDER_SIZE = 1  * 1024 * 1024 # 1GB
    MAX_IMAGE_FOLDER_SIZE = 200 * 1024 * 1024 # 200MB
    DOMAIN = [-88.0, -63.0, -25.0, 5.0]
    UMBRAL = 0.5

    SCHEDULER_API_ENABLED = True



