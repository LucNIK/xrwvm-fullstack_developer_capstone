import os
import requests
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# Retire les espaces / slash final éventuels
backend_url = backend_url.strip().rstrip("/")
sentiment_analyzer_url = sentiment_analyzer_url.strip()
if not sentiment_analyzer_url.endswith("/"):
    sentiment_analyzer_url += "/"


def get_request(endpoint, **kwargs):
    """GET vers le backend Express/Mongo."""
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += str(key) + "=" + str(value) + "&"

    request_url = backend_url + endpoint
    if params:
        request_url += "?" + params

    print("GET from {}".format(request_url))
    try:
        response = requests.get(request_url, timeout=10)
        return response.json()
    except Exception as err:
        print("Network exception occurred: {}".format(err))
        return None


def analyze_review_sentiments(text):
    """Appelle le microservice d'analyse de sentiment."""
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url, timeout=5)
        return response.json()
    except Exception as err:
        print("Unexpected error: {}".format(err))
        return {"sentiment": "neutral"}


def post_review(data_dict):
    """POST d'un avis vers le backend."""
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict, timeout=10)
        print(response.json())
        return response.json()
    except Exception as err:
        print("Network exception occurred: {}".format(err))
        return None
