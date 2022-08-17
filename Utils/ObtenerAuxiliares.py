import requests
import urllib
import traceback

def getElevation(lon,lat, errors):
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