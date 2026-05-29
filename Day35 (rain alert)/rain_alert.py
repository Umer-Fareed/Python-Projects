import requests
import smtplib


api_url = "https://api.openweathermap.org/data/2.5/weather"
api_key ="1c63106d351d9e43d14964e570ee8df0"

my_email = "experimental.my2@gmail.com"
password= "zvmj ajug fthq gzgh"

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
}

response = requests.get(api_url, params=weather_params)
weather_data= response.json()
print(response.json())
datapoint= (weather_data["weather"][0]["id"])
print(datapoint)
will_rain= False
if datapoint > 600 :
    will_rain= True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs= "experimental.my2@yahoo.com",
            msg= f"Subject: RainAlert\n\n"
                 f"It's rain outside pealse bring an umbrella"
        )

