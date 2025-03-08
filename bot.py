import requests
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

# Session Create karo
session = requests.Session()

def terabox_login():
    data = {
        "email": EMAIL,
        "password": PASSWORD
    }
    response = session.post(LOGIN_URL, data=data)
    if response.status_code == 200 and "success" in response.text:
        print("✅ Login Successful!")
        return True
    else:
        print("❌ Login Failed!")
        return False

def get_download_link(file_url):
    response = session.get(file_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        download_link = soup.find("a", {"class": "download-button"})
        if download_link:
            return download_link["href"]
    return None

def send_to_telegram(message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

def main():
    if terabox_login():
        file_url = input("Enter TeraBox File URL: ")
        download_link = get_download_link(file_url)
        if download_link:
            print("✅ Download Link:", download_link)
            send_to_telegram(f"TeraBox Download Link: {download_link}")
        else:
            print("❌ Failed to fetch download link!")

if __name__ == "__main__":
    main()
  
