import requests
import time
from bs4 import BeautifulSoup
from telegram import Bot

# Telegram Bot Token aur Chat ID yaha daalo
TELEGRAM_BOT_TOKEN = "7941445366:AAFwzqJBU5vRSzG83FUeAfRbZGNFfkecwFM"
TELEGRAM_CHAT_ID = "2128573817"

# TeraBox Login Credentials
EMAIL = "hackritesh16@gmail.com"
PASSWORD = "Ritesh123"

# TeraBox Login API URL
LOGIN_URL = "https://www.terabox.com/api/login"

# Proxy (Agar VPN ya Proxy use kar rahe ho to yaha daalo, warna None rakho)
PROXY = None  # "http://your_proxy_ip:port"

# Session Create karo
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive",
    "Referer": "https://www.terabox.com",
    "Origin": "https://www.terabox.com",
    "Content-Type": "application/x-www-form-urlencoded"
})

def terabox_login():
    data = {
        "email": EMAIL,
        "password": PASSWORD
    }
    
    time.sleep(5)
    
    try:
        response = session.post(LOGIN_URL, data=data, proxies={"http": PROXY, "https": PROXY} if PROXY else None)
        print("Response Code:", response.status_code)
        print("Response Text:", response.text)  # Debugging ke liye
        
        if response.status_code == 200:
            print("\n✅ Login Successful!")
            return True
        else:
            print("\n❌ Login Failed! Response:", response.text)
            return False
    except requests.exceptions.RequestException as e:
        print("\n❌ Connection Error:", e)
        return False

def main():
    if terabox_login():
        print("Bot is running...")
    else:
        print("Login failed. Check credentials or network settings.")

if __name__ == "__main__":
    main()
