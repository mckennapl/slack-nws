import json
import requests
from datetime import datetime
import weather_webhook # from weather_webhook.py

location_url = weather_webhook.loc # Examples tab https://www.weather.gov/documentation/services-web-api
webhook_url = weather_webhook.url
response = requests.get(location_url)
forecast = json.loads(response.text)

# Find time of day
def get_part_of_day(hour):
    return (
        ":sunflower: *Good morning!* :sunflower:" if 3 <= hour <= 11
        else
        ":sunny: *Good afternoon!* :sunny:" if 12 <= hour <= 17
        else
        ":city_sunset: *Good evening!* :city_sunset:" if 18 <= hour <= 22
        else
        ":moon: *Good night!* :moon:"
    )

time_of_day = datetime.now().hour

# Forecast variables
fc_forecast_time = forecast["properties"]["periods"][0]["name"]
fc_future_time = forecast["properties"]["periods"][1]["name"]
fc_forecast_short = forecast["properties"]["periods"][0]["shortForecast"]
fc_forecast_detailed = forecast["properties"]["periods"][0]["detailedForecast"]
fc_future_short =forecast["properties"]["periods"][1]["shortForecast"]
fc_future_detailed = forecast["properties"]["periods"][1]["detailedForecast"]

# The forecast
fc_whole_now = {"text": get_part_of_day(time_of_day) + "\n\n *Today's forecast calls for " + fc_forecast_short.lower() + ".* \n>" + fc_forecast_detailed + "\n\n\n*Later on " + fc_future_time.lower() + " will bring " + fc_future_short.lower() + ".* \n>" + fc_future_detailed}

# Create post
fc_0_time = requests.post(webhook_url, json = fc_whole_now)

# Post to Slack
print(fc_0_time)