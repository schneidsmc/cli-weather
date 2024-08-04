import sys
import requests
import json
import pyfiglet
from simple_chalk import chalk, green
import os
from dotenv import load_dotenv


load_dotenv()

def get_weather(zip_code, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={zip_code}"
    response = requests.get(url)
    if response.status_code != 200:
        return None, f"Error: Invalid response {response.status_code} from API."
    data = response.json()
    if 'error' in data:
        return None, "Error: Invalid zip code or other API error."
    return data, None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 weather.py <zip-code>")
        sys.exit(1)
    
    zip_code = sys.argv[1]
    api_key = os.getenv('API_KEY')
    
    weather_data, error = get_weather(zip_code, api_key)
    if error:
        print(error)
        sys.exit(1)
    
    weather = weather_data['current']['condition']['text']
    temperature = weather_data['current']['temp_f']
    city = weather_data['location']['name']
    art = pyfiglet.figlet_format(city)
    # print(f"{weather_data}")
    print(green.bold(f'{art}'))
    print(f"Currently, the weather for {chalk.bold.blue(zip_code)} is {chalk.bold.red(weather)} with a temperature of {chalk.bold.cyan(temperature)}°F!")

if __name__ == "__main__":
    main()

