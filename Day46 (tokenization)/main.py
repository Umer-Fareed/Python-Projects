import requests
from bs4 import BeautifulSoup
import smtplib
import os

my_email = "experimental.my2@gmail.com"
password = "zvmj ajug fthq gzgh"  # App password from Google

url = "https://www.amazon.com/BERIBES-Bluetooth-Headphones-Microphone-Lightweight/dp/B09LYF2ST7"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)

soup = BeautifulSoup(response.content, "lxml")

# Try to find price safely
price_tag = soup.find(class_="a-offscreen")
if not price_tag:
    print("Could not find price. Amazon may have blocked this request.")
    exit()

price = price_tag.get_text().strip()
price_as_float = float(price.replace("$", "").replace(",", ""))
print("Price:", price_as_float)

# Find title safely
title_tag = soup.find(id="productTitle")
title = title_tag.get_text().strip() if title_tag else "Unknown Product"
print("Title:", title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}\n{url}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}".encode("utf-8")
        )
    print("Email sent!")
else:
    print("No deal yet.")


