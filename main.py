import requests

API_KEY = 'TTBRBGMOSU9TZXIP'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

def getDataOfStock(stock):
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey": API_KEY
    }

    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    return response

def getYesterdayClosePrice(stock):
    response = getDataOfStock(stock)
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    yesterday_data = data_list[0]
    yesterday_close = yesterday_data["4. close"]
    
    return float(yesterday_close)

def getDayBeforeYesterdayClosePrice(stock):
    response = getDataOfStock(stock)
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    day_before_yesterday_data = data_list[1]
    day_before_yesterday_close = day_before_yesterday_data["4. close"]
    
    return float(day_before_yesterday_close)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

if __name__ == "__main__":
    yesterday_price = getYesterdayClosePrice(STOCK)
    day_before_yesterday_price = getDayBeforeYesterdayClosePrice(STOCK)
    difference = abs(yesterday_price - day_before_yesterday_price)
    difference_percent = (difference / yesterday_price) * 100
    if difference_percent >= 5: 
        print("Get news!")
