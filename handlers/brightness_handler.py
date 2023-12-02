from api_request import send_request
from utils.utils import get_lower_phrase

HIGH_BRIGHTNESS_PHRASES = [
    'сделай ярче',
    'увеличь яркость'
]

LOW_BRIGHTNESS_PHRASES = [
    'сделай темнее',
    'уменьши яркость'
]

SET_MAX_BRIGHTNESS_PHRASES = [
    'сделай максимально ярко',
    'установи максимальную яркость',
    'установи яркость на максимум'
]

SET_MIN_BRIGHTNESS_PHRASES = [
    'сделай максимально тускло',
    'установи минимальную яркость',
    'установи яркость на минимум'
]


def handle_brightness(req, res, main_url):
    brightness_change_phrases = {
        'increase': HIGH_BRIGHTNESS_PHRASES,
        'decrease': LOW_BRIGHTNESS_PHRASES,
        'setMax': SET_MAX_BRIGHTNESS_PHRASES,
        'setMin': SET_MIN_BRIGHTNESS_PHRASES,
    }

    for action, phrases in brightness_change_phrases.items():
        if get_lower_phrase(req) in phrases:
            handle_brightness_change(action, res, main_url)
            return True


def handle_brightness_change(action, res, main_url):
    res['response']['text'] = send_request(f'{main_url}/changeValue/{action}/brightness')
