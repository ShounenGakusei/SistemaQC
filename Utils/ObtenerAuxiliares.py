import requests
import urllib
import traceback
import pandas as pd

def getAuxiliarParams(path_base,params, extras, errors):


    codigo = params['codigo']
    if not codigo:
        lon = float(params['coordLon'])
        lat = float(params['coordLat'])

    stations = pd.read_csv(f'{path_base}/stations_data.csv')
    print(f'Estaciones: {path_base}/stations_data.csv')
    # Si se ha dado el codigo, colocamos defrente la Lon, Lat y Altitud
    if codigo:
        try:
            dfTemp = stations[stations['CODE']==codigo]
            if not dfTemp.empty:
                data = dfTemp.iloc[0]
                extras['alt'] = data['ALT']
                extras['umb1'] = data['Umbral1']
                params['coordLon'] = float(data['LON'])
                params['coordLat'] = float(data['LAT'])
                return True

        except Exception as e:
            traceback.print_exc()
            errors['auxVar'] = [f'ERROR AL INTENTAR ENCONTRAR LAS VARIABLES AUXILIARES POR CODIGO {str(e)}']
            return False

    # Buscamos Lon, lat para hallar Altitud
    try:
        dfTemp = stations[(abs(stations['LON'] - lon) < 0.0001) & ((stations['LAT'] - lat) < 0.0001)]
        if not dfTemp.empty:
            data = dfTemp.iloc[0]
        else: # Buscamos el mas cercano
            dfTemp['difLon'] = abs(dfTemp['LON'] - lon)
            dfTemp['difLat'] = abs(dfTemp['LAT'] - lat)
            dfTemp['dif'] = dfTemp['difLon'] + dfTemp['difLat']
            data = dfTemp.sort_values('dif', ascending=True).head(1)

        print('DataEstacion:' , data)
        extras['alt'] = data['ALT']
        extras['umb1'] = data['Umbral1']
        return True

    except Exception as e:
        traceback.print_exc()
        errors['auxVar'] = [f'ERROR AL INTENTAR ENCONTRAR LAS VARIABLES AUXILIARES {str(e)}']
        return False


def getElevation(path_base,lon,lat, errors):
    url = r'https://nationalmap.gov/epqs/pqs.php?'

    # define rest query params
    params = {
        'output': 'json',
        'x': lon,
        'y': lat,
        'units': 'Meters'
    }

    # format query string and return query value
    result = requests.get((url + urllib.parse.urlencode(params)))
    try:
        lat = result.json()['USGS_Elevation_Point_Query_Service']['Elevation_Query']['Elevation']
    except Exception as e:
        traceback.print_exc()
        errors['Elevacion'] = f'No se pudo conseguir la altura para {lon}, {lat}: {str(e)}'
        errors['valido'] = False
        return 0

    return lat