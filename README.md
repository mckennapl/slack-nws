# slack-nws

Python script to capture short and detailed NWS forecasts from their API and then post those to a Slack team and channel of your choosing.

Needs a weather_webhook.py file with your location and webhook URL:

### weather_webhook.py
```
url = "https://hooks.slack.com/services/XXXXXXXX/YYYYYYYYYY/ZZZZZZZZZZZZZZZZ"
loc = "https://api.weather.gov/gridpoints/{office}/{grid_x},{grid_y}/forecast/" #check the examples tab at https://www.weather.gov/documentation/services-web-api
```
