from handlers.animation_smooth_handler import handle_animation_smooth
from handlers.brightness_handler import handle_brightness
from handlers.color_handler import handle_color
from handlers.modes_handler import handle_modes
from handlers.rainbow_step_handler import handle_rainbow_step
from handlers.saturation_handler import handle_saturation
from handlers.speed_handler import handle_speed
from handlers.temperature_handler import handle_temperature

from utils.utils import get_lower_phrase, get_error_phrase


def handle_dialog(req, res, main_url):
    if req['session']['new'] or get_lower_phrase(req) in ['что ты умеешь', 'помощь']:
        res['response']['text'] = 'привет! я могу управлять подсветкой!'
        res['response']['tts'] = 'прив+ет! sil <[500]> я мог+у управл+ять подсв+еткой!'
        return
    elif get_lower_phrase(req) in ['закончить диалог', 'завершить диалог']:
        res['response']['text'] = 'Пока!'
        res['response']['end_session'] = True

    elif handle_modes(req, res, main_url):
        return
    elif handle_temperature(req, res, main_url):
        return
    elif handle_brightness(req, res, main_url):
        return
    elif handle_saturation(req, res, main_url):
        return
    elif handle_speed(req, res, main_url):
        return
    elif handle_rainbow_step(req, res, main_url):
        return
    elif handle_animation_smooth(req, res, main_url):
        return
    elif handle_color(req, res, main_url):
        return
    else:
        res['response']['text'] = get_error_phrase()
        return
