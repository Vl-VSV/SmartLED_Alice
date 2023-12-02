from api_request import send_request
from utils.utils import get_lower_phrase

INCREASE_ANIMATION_SMOOTH_PHRASES = [
    'увеличь плавность',
    'сделай анимацию плавнее'
]

DECREASE_ANIMATION_SMOOTH_PHRASES = [
    'уменьши плавность',
    'сделай анимацию менее плавной'
]

SET_MAX_ANIMATION_SMOOTH_PHRASES = [
    'установи максимальную плавность',
    'сделай максимально плавной анимацию',
    'сделай анимацию максимально плавной'
]

SET_MIN_ANIMATION_SMOOTH_PHRASES = [
    'установи минимальную плавность',
    'сделай минимально плавной анимацию',
    'сделай анимацию минимально плавной'
]


def handle_animation_smooth(req, res, main_url):
    animation_smooth_change_phrases = {
        'increase': INCREASE_ANIMATION_SMOOTH_PHRASES,
        'decrease': DECREASE_ANIMATION_SMOOTH_PHRASES,
        'setMax': SET_MAX_ANIMATION_SMOOTH_PHRASES,
        'setMin': SET_MIN_ANIMATION_SMOOTH_PHRASES,
    }

    for action, phrases in animation_smooth_change_phrases.items():
        if get_lower_phrase(req) in phrases:
            handle_animation_smooth_change(action, res, main_url)
            return True


def handle_animation_smooth_change(action, res, main_url):
    res['response']['text'] = send_request(f'{main_url}/changeValue/{action}/animation_smooth')
