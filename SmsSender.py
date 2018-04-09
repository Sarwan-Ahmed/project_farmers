import pyowm
from twilio.rest import Client


def send_sms(location):
    temperature = get_weather(location)
    twilio_account_key = "ACa39fd545325f4845fefc002afbad0bdf"
    twilio_authentication_token = "ef13b9832edea362b9fa9f663d32b18e"
    client = Client(twilio_account_key, twilio_authentication_token)
    client.messages.create(to="+923353187436", from_="+19172424541",
                           body="Today temperature at "+ location+" is "+ str(temperature)+"'C")



def get_weather(location):
    apiKey = 'a1db274fcb4e9a13a14e52e569c6fd1a'
    openWeatherClient = pyowm.OWM(apiKey)
    observation = openWeatherClient.weather_at_place(location)
    weather = observation.get_weather()
    temperature = weather.get_temperature('celsius')['temp']
    return temperature
