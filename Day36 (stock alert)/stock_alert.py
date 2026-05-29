import requests
import smtplib
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY= "RP25EDO2LJJJA557"
NEWS_API_KEY= "008e76973f854ef4bd6ce7860b680603"

my_email = "experimental.my2@gmail.com"
password= "zvmj ajug fthq gzgh"
send_mail= "experimental.my2@yahoo.com"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price

stock_parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
                }
response= requests.get(url= STOCK_ENDPOINT,params=stock_parameters)
data= response.json()["Time Series (Daily)"]
print(data)
data_list= [value for  (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price  = yesterday_data["4. close"]
print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
day_before_yesterday = data_list[1]
day_before_closing_price = float(day_before_yesterday["4. close"])
print(day_before_closing_price)

#Find the difference between 1 and 2
price_diff = float(yesterday_closing_price) - float(day_before_closing_price)


up_down= None
if price_diff > 0 :
    up_down= "🔺"
else:
    up_down= "🔻"

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = round((price_diff / float(yesterday_closing_price)) * 100)
print(f"Percentage difference: {percentage_diff}%")


 ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(percentage_diff) > 1:
    news_params= {
        "q":COMPANY_NAME,
        "sortBy":"popularity&",
        "apikey":NEWS_API_KEY
    }
    response_2= requests.get(url= "https://newsapi.org/v2/everything",params= news_params)
    articles= (response_2.json()["articles"])
    print(articles)
    # Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    ## STEP 3: Use Twilio to send a seperate message with each article's title and description to your phone number.

    # Create a new list of the first 3 articles headline and description using list comprehension.
    formatted_articles= [f"{STOCK_NAME}: {up_down}{percentage_diff}% \n Headline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    # Send each article as a separate message via Twilio
    for article in formatted_articles:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            msg = f"Subject: Stock Alert\nContent-Type: text/plain; charset=utf-8\n\n{article}"
            connection.sendmail(
                from_addr=my_email,
                to_addrs="experimental.my2@yahoo.com",
                msg=msg.encode("utf-8")
            )

