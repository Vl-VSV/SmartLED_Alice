from api_request import send_request
from utils.utils import get_lower_phrase

INCREASE_RAINBOW_STEP_PHRASES = [
    'увеличь шаг радуги'
]

DECREASE_RAINBOW_STEP_PHRASES = [
    'уменьши шаг радуги'
]

SET_MAX_RAINBOW_STEP_PHRASES = [
    'установи максимальный шаг радуги',
    'поставь шаг радуги на максимум'
]

SET_MIN_RAINBOW_STEP_PHRASES = [
    'установи минимальный шаг радуги',
    'поставь шаг радуги на минимум'
]


def handle_rainbow_step(req, res, main_url):
    rainbow_step_change_phrases = {
        'increase': INCREASE_RAINBOW_STEP_PHRASES,
        'decrease': DECREASE_RAINBOW_STEP_PHRASES,
        'setMax': SET_MAX_RAINBOW_STEP_PHRASES,
        'setMin': SET_MIN_RAINBOW_STEP_PHRASES,
    }

    for action, phrases in rainbow_step_change_phrases.items():
        if get_lower_phrase(req) in phrases:
            handle_rainbow_step_change(action, res, main_url)
            return True


def handle_rainbow_step_change(action, res, main_url):
    res['response']['text'] = send_request(f'{main_url}/changeValue/{action}/rainbow_step')