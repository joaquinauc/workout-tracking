import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv("keys.env")

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

print(API_KEY)

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_query = {
    "query": input("Tell me which exercises you did: ")
}

response = requests.post(url=exercise_endpoint, json=exercise_query, headers=exercise_headers)
print(response.text)

exercise_data = response.json()["exercises"][0]

today = datetime.now()

sheety_body = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise_data["name"].title(),
        "duration": round(exercise_data["duration_min"]),
        "calories": round(exercise_data["nf_calories"])
    }
}

sheety_headers = {
    "Authorization": AUTH_TOKEN
}

response_sheety = requests.post(url=SHEET_ENDPOINT, json=sheety_body, headers=sheety_headers)
# print(response_sheety.text)
