import os
import requests
from utils.utils import get_ready_phrase


def get_token():
    return os.environ['AUTH_TOKEN']


def send_request(req):
    headers = {
        'Authorization': f'Api-Key {get_token()}'
    }
    response = requests.get(req, headers=headers)
    if response.status_code == 200:
        return get_ready_phrase()
    else:
        return response.json().get('detail')
