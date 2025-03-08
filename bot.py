import requests
import time
import cloudscraper
from bs4 import BeautifulSoup
from telegram import Bot

# Telegram Bot Token aur Chat ID
TELEGRAM_BOT_TOKEN = "7941445366:AAFwzqJBUS"
TELEGRAM_CHAT_ID = "2128573817"

# TeraBox Login Credentials
EMAIL = "hackritesh16@gmail.com"
PASSWORD = "Ritesh123"

# TeraBox Login API URL
LOGIN_URL = "https://www.terabox.com/api/login"

# Proxy (Agar VPN ya Proxy use kar rahe ho to yaha daalo, warna None rakho)
PROXY = None  # "http://your_proxy_ip:port"

# Cloudflare bypass ke liye scraper session
session = cloudscraper.create_scraper()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.terabox.com/",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
})

def terabox_login():
    data = {
        "email": EMAIL,
        "password": PASSWORD
    }
    
    # Delay to avoid getting blocked
    time.sleep(5)
    
    try:
        response = session.post(LOGIN_URL, data=data, proxies={"http": PROXY, "https": PROXY} if PROXY else None)
        response.raise_for_status()
        
        if response.status_code == 200:
            print("Login successful!")
            return True
        else:
            print("Login failed! Status Code:", response.status_code)
            return False
    except requests.exceptions.RequestException as e:
        print("Connection Error:", e)
        return False

def main():
    if terabox_login():
        print("Bot is running...")
    else:
        print("Login failed. Check credentials or network settings.")

if __name__ == "__main__":
    main()
