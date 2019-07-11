import requests
import time
from datetime import datetime


bitcoin_api = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
my_bit_threshold = 10000

# 2. Sending a Test IFTTT Notification to my phone
my_webhook_url = "https://maker.ifttt.com/trigger/flow_test/with/key/6n_9v5GZTrP43IKyAO_yW"


def get_latest_bitcoin_price():
    # Sending an HTTP GET request
    r = requests.get(bitcoin_api)

    # Converting JSON r into python object
    json_response = r.json()

    # Convert the USD price to a floating point number
    return float(json_response[0]['price_usd'])


# def my_webhook(event, value):
#     # The payload that will be sent to IFTTT service
#     data = {'value1': value}
#
#     # inserts our desired event
#     idtt_event_url = my_webhook_url.format(event)
#
#     # sends a HTTP POST request to the webhook URL
#     requests.post(my_webhook_url, json=data)


def format_bit_history(bit_history):
    rows = []
    # Formats the date into a string: '02.10.2019 10:41'
    for bit_price in bit_history:
        date = bit_price['date'].strftime("%m.%d.%Y %H:%M")
        price = bit_price['price']
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)

        return '<br>'.join(rows)


# def main():
#     bit_history = []
#     while True:
#         price = get_latest_bitcoin_price()
#         date = datetime.now()
#         bit_history.append({'date': date, 'price': price})
#
#         # Send an emergency notification
#         if price < my_bit_threshold:
#             my_webhook('emergency_bitcoin_price', price)
#
#         # Send a Telegram notification
#         if len(bit_history) == 10:
#             my_webhook('bitcoin_update', format_bit_history(bit_history))
#
#             # Reset history
#             bit_history = []
#
#         # Sleep for 5 minutes
#         time.sleep(5 * 60)


if __name__ == '__main__':
    main()



