import requests
import json
from io import BytesIO
from PIL import Image

# airvisualapi_key = "your_airvisual_api_key"
# openweatherapi_key = "your_openweather_api_key"
airvisualapi_key = "Your_AirVisual_API_code" #https://www.iqair.com/vietnam/da-nang  create an account
openweatherapi_key = "Youe_Openwaether_API_code" #https://openweathermap.org/api  create an account


def get_data():
    # Get latitude and longitude of nearest city from Air Visual
    url = "http://api.airvisual.com/v2/nearest_city?key=" + airvisualapi_key
    response = requests.request('GET', url)
    raw_data = json.loads(response.text)
    measurements = []
    # print(raw_data)
    lon = raw_data["data"]["location"]["coordinates"][0]
    lat = raw_data["data"]["location"]["coordinates"][1]
    print("Latitude is ", lat, "Longitude is ", lon)
    # Get weather from OpenWeather using latitude and longitude from Air Visua;
    exclude = "current,minutely,daily"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude={}&appid={}".format(
        lat, lon, exclude, openweatherapi_key)
    response = requests.get(url)
    data = json.loads(response.text)
    # to make data more readable
    #data = json.dumps(data, indent=4) This prints the json in a readable format
    print(data)
    return data
