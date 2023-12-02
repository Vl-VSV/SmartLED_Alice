from api_request import send_request
from utils.utils import get_lower_phrase

INCREASE_SATURATION_PHRASES = [
    'увеличь насыщенность'
]

DECREASE_SATURATION_PHRASES = [
    'уменьши насыщенность'
]

SET_MAX_SATURATION_PHRASES = [
    'установи максимальную насыщенность'
]

SET_MIN_SATURATION_PHRASES = [
    'установи минимальную насыщенность'
]


def handle_saturation(req, res, main_url):
    saturation_change_phrases = {
        'increase': INCREASE_SATURATION_PHRASES,
        'decrease': DECREASE_SATURATION_PHRASES,
        'setMax': SET_MAX_SATURATION_PHRASES,
        'setMin': SET_MIN_SATURATION_PHRASES,
    }

    for action, phrases in saturation_change_phrases.items():
        if get_lower_phrase(req) in phrases:
            handle_saturation_change(action, res, main_url)
            return True


def handle_saturation_change(action, res, main_url):
    res['response']['text'] = send_request(f'{main_url}/changeValue/{action}/saturation')
