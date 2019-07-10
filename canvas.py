import requests
import time
from datetime import datetime


# 1. Retrieving Bitcoin price
# Sending an HTTP GET request to the URL using the requests.get() function. This should return a json response.
b_api = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"

# 2. Sending a Test IFTTT Notification to my phone
my_webhook_url = "https://maker.ifttt.com/trigger/flow_test/with/key/6n_9v5GZTrP43IKyAO_yW"


def get_latest_bitcoin_price():
    response = requests.get(b_api)

    # Converting JSON response into python object
    response_json = response.json()

    # Convert the USD price to a floating point number
    return float(response_json[0]['price_usd'])


def my_webhook(event, value):
    # The payload that will be sent to IFTTT service
    data = {'value1': value}

    # inserts our desired event
    idtt_event_url = my_webhook_url.format(event)

    #sends a HTTP POST request to the webhook URL
    requests.post(my_webhook_url, json=data)


my_bit_threshold = 10000


def main():
    bit_history = []
    while True:
        price = get_latest_bitcoin_price()
        date = datetime.now()







def if __name__ == '__main__':
    main()



