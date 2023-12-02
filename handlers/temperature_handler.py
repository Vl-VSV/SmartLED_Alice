from api_request import send_request
from utils.utils import get_lower_phrase

INCREASE_TEMPERATURE_PHRASES = [
    'сделай цвет теплее',
    'сделай цвет более теплым',
]

DECREASE_TEMPERATURE_PHRASES = [
    'сделай цвет холоднее',
    'сделай цвет более холодным'
]

SET_MAX_TEMPERATURE_PHRASES = [
    'сделай цвет максимально теплым'
]

SET_MIN_TEMPERATURE_PHRASES = [
    'сделай цвет максимально холодным'
]


def handle_temperature(req, res, main_url):
    temperature_change_phrases = {
        'increase': INCREASE_TEMPERATURE_PHRASES,
        'decrease': DECREASE_TEMPERATURE_PHRASES,
        'setMax': SET_MAX_TEMPERATURE_PHRASES,
        'setMin': SET_MIN_TEMPERATURE_PHRASES,
    }

    for action, phrases in temperature_change_phrases.items():
        if get_lower_phrase(req) in phrases:
            handle_temperature_change(action, res, main_url)
            return True


def handle_temperature_change(action, res, main_url):
    res['response']['text'] = send_request(f'{main_url}/changeValue/{action}/temperature')
