from api_request import send_request
from utils.utils import get_lower_tokens

INCREASE_SPEED_PHRASES = [
    'увеличь скорость'
]

DECREASE_SPEED_PHRASES = [
    'уменьши скорость'
]

SET_MAX_SPEED_PHRASES = [
    'установи максимальную скорость'
]

SET_MIN_SPEED_PHRASES = [
    'установи минимальную скорость'
]


def handle_speed(req, res, main_url):
    speed_change_phrases = {
        'increase': INCREASE_SPEED_PHRASES,
        'decrease': DECREASE_SPEED_PHRASES,
        'setMax': SET_MAX_SPEED_PHRASES,
        'setMin': SET_MIN_SPEED_PHRASES,
    }

    for action, phrases in speed_change_phrases.items():
        if get_lower_tokens(req) in phrases:
            handle_speed_change(action, res, main_url)
            return True


def handle_speed_change(action, res, main_url):
    res['response']['text'] = send_request(f'{main_url}/changeValue/{action}/speed')
