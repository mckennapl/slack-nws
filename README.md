# slack-nws

Python script to capture the short and the detailed NWS forecasts from their API and then post to a Slack channel.

You'll need to have Incoming Webhooks set up on your Slack: https://api.slack.com/messaging/webhooks

Create a weather_webhook.py (in .gitignore) file with your location and webhook URL:

### weather_webhook.py
```
url = "https://hooks.slack.com/services/XXXXXXXX/YYYYYYYYYY/ZZZZZZZZZZZZZZZZ"
loc = "https://api.weather.gov/gridpoints/{office}/{grid_x},{grid_y}/forecast/" #check the examples tab at https://www.weather.gov/documentation/services-web-api
```

## To-dos

* Make the output prettier
* Create alerting for NWS alerts
