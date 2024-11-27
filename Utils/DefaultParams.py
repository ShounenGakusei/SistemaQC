def getDefaultParams(path_base):

    params = {
        # Parametros fijos
        'domain': [-88.0, -63.0, -25.0, 5.0],  # [-83.5495, -66.4504, -20.2252, 1.3783],
        'canales': ['13', '07', '08'],#['07', '08', '13'],
        'tiempos': ['00', '30', '50'],#['00', '30', '50'],#['50', '30', '00'], #['00', '50', '40', '30'],
        'margen': 8,

        # Parametros auxiliares
        'dibujar': False,
        'canalDibujar': '13',
        'save': True,
        'hard_save': False,
        "sizeMax": 2000000,
        "saveMax": 10000000,
        'umbral': 0.51,
        'port' : 8080,
    }

    return params