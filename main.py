import requests
from twilio.rest import Client
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="MyApp")
city = input("Enter location in city,country format: ")

location = geolocator.geocode(city)

api_key = "e33c20d284c41150622d7569a36706e6"
LAT = location.latitude
LONG = location.longitude
account_sid = "ACeceb5af6c0fb0be6f69f951d269f3811"
auth_token = "04b28892dea27567203e2407289c5b6b"
parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"]
will_rain = False

for data in range(12):
    weather_id = hourly_data[data]['weather'][0]['id']
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today make sure to bring an ☂️ ",
        from_='+12705144877',
        to='+918275676705'
    )
    print(message.status)
