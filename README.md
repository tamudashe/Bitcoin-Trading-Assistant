# Bitcoin Trading Assistant
This project provides notifications about Bitcoin prices. Assists in when to buy or when to sell depending on the set threshold.

![Bitcoin](https://images.pexels.com/photos/1036635/pexels-photo-1036635.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)

## API used: [Coinmarketcap API](https://coinmarketcap.com/api/documentation/v1/#)

## Technology used: Python 3

## Modules Used :
* requests 
* time 
* datetime

#### Get latest bitcoin price:
1. Send an HTTP request
2. Convert JSON response into a python object
3. Locate the USD price and convert the string into a number
