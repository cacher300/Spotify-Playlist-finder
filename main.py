import requests
import random
import string
import sys

def check_website_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        print(f"URL: {url}")
        print(f"Status Code: {status_code}")

        # Check the status code and print a corresponding message
        if status_code == 200:
            print("Success: The request was successful.")
            print(f"URL: {url}")
            sys.exit()

        elif status_code == 404:
            print("Error 404: The requested resource could not be found.")
        elif status_code == 500:
            print("Error 500: Internal Server Error.")
        else:
            print(f"Received HTTP status code {status_code}.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def generate_random_string(length):
    characters = string.ascii_letters + string.digits

    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string


string_length = 22  

try:
    i = 1
    while True:
        random_string = generate_random_string(string_length)
        url_to_check = f"https://open.spotify.com/playlist/{random_string}"
        check_website_status(url_to_check)

        i += 1
except KeyboardInterrupt:
    print("Generation stopped")

