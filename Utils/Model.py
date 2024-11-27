import os
import traceback

import numpy as np
import tensorflow as tf

from Utils.ObtenerModelo import crearModelo


class Model():
    modelos = []
    params = {}
    errors = []
    valido = True
    def __init__(self, params):
        self.params = params
        self.inicializado = False

    def iniciarModelos(self):
        # Reseteamos las variables
        self.modelos = []
        self.inputLayers = []
        self.errors = []
        self.valido = True

        modelos_file = [f'{self.params["dirModelos"]}{e}' for e in os.listdir(self.params["dirModelos"])]
        modelos_file = [e for e in modelos_file if '.hdf5' in e]
        if len(modelos_file) == 0:
            self.errors.append('No se encontraron los modelos')
            self.valido = False
            return 

        print(f'Cantidad de modelos leidos: {len(modelos_file)}')

        for mWeigts in modelos_file:
            try:
                modelo = tf.keras.models.load_model(mWeigts)
                self.modelos.append(modelo)
            except:
                self.errors.append(f'No se pudo agregar el modelo {mWeigts}')
                self.valido = False
                return 

            if len(self.modelos) == 0:
                self.errors.append(f'No se logro leer ningun modelo algoritmico')
                self.valido = False
                return 
        self.inicializado = True

    def predecirValor(self, imagen, dato, extras={}):
        errores = []
        predicciones = []

        conforme = 0
        malo = 0
        nc = 0

        if not self.inicializado and self.valido:
            self.iniciarModelos()

        # En caso no se pueda inicializar, se retorna error
        if not self.valido:
            return [0],0,0,0, self.errors


        for modelo in self.modelos:
            inputLayers = []
            config = modelo.get_config()
            for layer in config['layers']:
                if layer['class_name'] == 'InputLayer':
                    inputLayers.append(layer['name'])
            try:
                prediction = modelo.predict({inputLayers[0]: np.full((1, imagen.shape[0], imagen.shape[1],
                                                                          imagen.shape[2], imagen.shape[3]),
                                                                         imagen),
                                             inputLayers[1]: np.full((1,), dato), # 2
                                             inputLayers[3]: np.full((1,), float(extras['alt'])), #3
                                             inputLayers[2]: np.full((1,), float(extras['umb1'])) # 1
                                             }, verbose=0)
                print('Prediccion: ', prediction)
                predicciones.append(prediction[0,0])

            except Exception:
                traceback.print_exc()
                pass

        if len(predicciones) == 0:
            errores.append(f'Error al intentar predecir la clasificacion para el valor de precipitacion con el modelo')
            

        for p in predicciones:
            if p > float(extras['umbral']): #p > self.params['umbral']:
                conforme = conforme + 1
            else:
                malo = malo +1

        return predicciones, nc, malo, conforme, errores
