import requests

MAIN_URL = 'https://smartled.onrender.com'


def main(event, context):
    response = {
        'session': event['session'],
        'version': event['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(event, response)
    return response


def get_lower_tokens(request):
    return [x.lower() for x in request['request']['nlu']['tokens']]


def get_ready_phrase():
    return "Готово!"


def handle_dialog(req, res):
    if req['session']['new']:
        res['response']['text'] = 'Привет! Я могу управлять подсветкой!'
        res['response']['tts'] = 'прив+ет! sil <[500]> я мог+у управл+ять подсв+еткой'

    elif get_lower_tokens(req) in [['закончить', 'диалог'], ['завершить', 'диалог']]:
        res['response']['text'] = 'Пока!'
        res['response']['tts'] = 'Пока!'
        res['response']['end_session'] = True

    elif get_lower_tokens(req) in [['что', 'ты', 'умеешь'], ['помощь']]:
        res['response']['text'] = 'Привет! Я могу управлять подсветкой!'
        res['response']['tts'] = 'прив+ет! sil <[500]> я мог+у управл+ять подсв+еткой'

    # Смена режимов
    elif get_lower_tokens(req) == ['включи', 'белый', 'свет']:
        requests.put(f'{MAIN_URL}/setModeAndSubmode?new_mode=1&new_submode=1')
        res['response']['text'] = 'Готово!'
    elif get_lower_tokens(req) == ['включи', 'постоянный', 'цвет']:
        requests.put(f'{MAIN_URL}/setModeAndSubmode?new_mode=1&new_submode=2')
        res['response']['text'] = 'Готово!'
    elif get_lower_tokens(req) == ['включи', 'плавную', 'смену', 'цветов']:
        requests.put(f'{MAIN_URL}/setModeAndSubmode?new_mode=1&new_submode=3')
        res['response']['text'] = 'Готово!'

    elif get_lower_tokens(req) == ['включи', 'радугу']:
        requests.put(f'{MAIN_URL}/setModeAndSubmode?new_mode=2&new_submode=1')
        res['response']['text'] = 'Готово!'
    elif get_lower_tokens(req) == ['включи', 'конфетти']:
        requests.put(f'{MAIN_URL}/setModeAndSubmode?new_mode=2&new_submode=2')
        res['response']['text'] = 'Готово!'
    elif get_lower_tokens(req) == ['включи', 'бегающую', 'точку']:
        requests.put(f'{MAIN_URL}/setModeAndSubmode?new_mode=2&new_submode=3')
        res['response']['text'] = 'Готово!'
    elif get_lower_tokens(req) == ['включи', 'огонь']:
        requests.put(f'{MAIN_URL}/setModeAndSubmode?new_mode=2&new_submode=4')
        res['response']['text'] = 'Готово!'
    elif get_lower_tokens(req) == ['включи', 'лаву']:
        requests.put(f'{MAIN_URL}/setModeAndSubmode?new_mode=2&new_submode=5')
        res['response']['text'] = 'Готово!'
    elif get_lower_tokens(req) == ['включи', 'облака']:
        requests.put(f'{MAIN_URL}/setModeAndSubmode?new_mode=2&new_submode=6')
        res['response']['text'] = 'Готово!'

    # Теплота
    elif get_lower_tokens(req) in [['сделай', 'цвет', 'теплее']]:
        response = requests.get(f'{MAIN_URL}/changeValue/increase/temperature')
        res['response']['text'] = get_ready_phrase() if response.status_code == 200 else response.headers['detail']
    elif get_lower_tokens(req) in [['сделай', 'цвет', 'холоднее']]:
        response = requests.get(f'{MAIN_URL}/changeValue/decrease/temperature')
        res['response']['text'] = get_ready_phrase() if response.status_code == 200 else response.headers['detail']
    elif get_lower_tokens(req) in [['сделай', 'цвет', 'максимально', 'теплым']]:
        response = requests.get(f'{MAIN_URL}/changeValue/setMax/temperature')
        res['response']['text'] = get_ready_phrase() if response.status_code == 200 else response.headers['detail']
    elif get_lower_tokens(req) in [['сделай', 'цвет', 'максимально', 'холодным']]:
        response = requests.get(f'{MAIN_URL}/changeValue/setMin/temperature')
        res['response']['text'] = get_ready_phrase() if response.status_code == 200 else response.headers['detail']

    else:
        res['response']['text'] = 'Я не знаю, что ответить'
