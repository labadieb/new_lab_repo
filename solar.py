#!/usr/bin/env python3
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

now = datetime.now()
ASTRONOMYAPI_ID="f9c55886-d088-444a-9263-9a31ab9c503b"
ASTRONOMYAPI_SECRET="c258c7d9e4f0c8ff238d8a40bac1614e1d987605840212af1393840c629de92ff41a45c78490c9dc2a503c2a70b9de12be33eaf989904493e25938bdb2e3afb1a123154fd79fa7db1bd7210014c5a3fd51cf19c734771c14c105f5195c8381f95b016b963774620ba9649a481d049b59"

def get_sun_position(latitude, longitude, body = 'sun'):
    """Returns the current position of the sun in the sky at the specified location
    Parameters:
    latitude (str)
    longitude (str)
    Returns:
    float: azimuth
    float: altitude
    """
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'elevation': 0,
        'from_date': now.date().isoformat(),
        'to_date': now.date().isoformat(),
        'time': now.strftime('%H:%M:%S')
        }
    response = requests.get('https://api.astronomyapi.com/api/v2/bodies/positions/sun', auth = (ASTRONOMYAPI_ID,ASTRONOMYAPI_SECRET), params=payload )
    print(response.text)

    response = response.json()
    body_data = response['data']['table']['rows'][0]['cells'][0]
    position = body_data['position']['horizontal']
    alt = position['altitude']['degrees']
    az = position['azimuth']['degrees']
    # NOTE: Replace with your real return values!
    return az, alt
    
def print_position(azimuth, altitude):
    """Prints the position of the sun in the sky using the supplied coordinates
    Parameters:
    azimuth (float)
    altitude (float)"""

    print("The Sun is currently at:")
    print(f'{altitude} deg altitude, {azimuth} deg azimuth')

def get_location():
    
    response = requests.get('http://ip-api.com/json/?fields=lat,lon')
   
    latitude = response.json()['lat']
    longitude = response.json()['lon']
    
    return latitude,longitude

if __name__ == "__main__":
    latitude, longitude = get_location()
    azimuth, altitude = get_sun_position(latitude,longitude)
    print_position(azimuth, altitude)
