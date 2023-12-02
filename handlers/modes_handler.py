from api_request import send_request
from utils.utils import get_lower_tokens, get_lower_phrase

MODES_AND_SUBMODES = {
    'белый свет': (1, 1),
    'постоянный цвет': (1, 2),
    'плавную смену цветов': (1, 3),
    'радугу': (2, 1),
    'конфетти': (2, 2),
    'бегающую точку': (2, 3),
    'огонь': (2, 4),
    'лаву': (2, 5),
    'облака': (2, 6)
}


def handle_modes(req, res, main_url):
    if get_lower_phrase(req) in ['какой режим', 'какой сейчес режим']:
        res['response']['text'] = send_request(f'{main_url}/whatMode')
        return True

    elif get_lower_phrase(req) in ['следующий режим']:
        res['response']['text'] = send_request(f'{main_url}/setNextMode')
        return True

    elif get_lower_phrase(req) in ['прошлый режим', 'предыдущий режим']:
        res['response']['text'] = send_request(f'{main_url}/setPreviousMode')
        return True

    nlu_tokens = get_lower_tokens(req)
    if len(nlu_tokens) == 0 or nlu_tokens[0] != 'включи':
        return

    mode_key = ' '.join(nlu_tokens[1:])
    if mode_key in MODES_AND_SUBMODES:
        new_mode, new_submode = MODES_AND_SUBMODES[mode_key]
        res['response']['text'] = send_request(
            f'{main_url}/setModeAndSubmode?new_mode={new_mode}&new_submode={new_submode}')
        return True
