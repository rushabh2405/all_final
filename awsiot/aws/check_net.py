import time
import requests

def check_internet():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        response.raise_for_status()
        return True
    except:
        return False

while True:
    if check_internet():
        print("Internet is available.")
    else:
        print("Internet is not available.")
    time.sleep(1)
