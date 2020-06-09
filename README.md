# slack-nws

![Weather Boi in Action](https://i.imgur.com/JeZaqwY.png)

Python script to capture the short and the detailed NWS forecasts from their API and then post to a Slack channel.

You'll need to have Incoming Webhooks set up on your Slack: https://api.slack.com/messaging/webhooks

## Usage

Create a weather_webhook.py file with your location and webhook URL:

### weather_webhook.py
```
url = "https://hooks.slack.com/services/XXXXXXXX/YYYYYYYYYY/ZZZZZZZZZZZZZZZZ"
loc = "https://api.weather.gov/gridpoints/{office}/{grid_x},{grid_y}/forecast/" #check the examples tab at https://www.weather.gov/documentation/services-web-api
```
As the comment says you'll also need to check the examples tab on https://www.weather.gov/documentation/services-web-api to figure out your office and grid axises.

## To-dos

* ~Make the output prettier~
* Add dynamic emojis based on weather
* Create alerting for NWS alerts
