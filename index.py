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

    # Изменение деталей [settings[0]]
    elif get_lower_tokens(req) in [['сделай', 'цвет', 'теплее'],
                                   ['увеличь', 'скорость']]:
        requests.get(f'{MAIN_URL}/setSet0Higher')
        res['response']['text'] = 'Готово!'
    elif get_lower_tokens(req) in [['сделай', 'цвет', 'холоднее'],
                                   ['уменьши', 'скорость']]:
        requests.get(f'{MAIN_URL}/setSet0Lower')
        res['response']['text'] = 'Готово!'
    elif get_lower_tokens(req) in [['сделай', 'цвет', 'максимально', 'теплым'],
                                   ['установи', 'минимальную', 'скорость']]:
        requests.get(f'{MAIN_URL}/setSet0Max')
        res['response']['text'] = 'Готово!'
    elif get_lower_tokens(req) in [['сделай', 'цвет', 'максимально', 'холодным'],
                                   ['установи', 'максимальную', 'скорость']]:
        requests.get(f'{MAIN_URL}/setSet0Min')
        res['response']['text'] = 'Готово!'

    # Изменение деталей [settings[1]]
    elif get_lower_tokens(req) in [['увеличь', 'яркость'],
                                   ['увеличь', 'насыщенность']]:
        requests.get(f'{MAIN_URL}/setSet1Higher')
        res['response']['text'] = 'Готово!'
    elif get_lower_tokens(req) in [['уменьши', 'яркость'],
                                   ['уменьши', 'насыщенность']]:
        requests.get(f'{MAIN_URL}/setSet1Lower')
        res['response']['text'] = 'Готово!'
    elif get_lower_tokens(req) in [['установи', 'максимальную', 'яркость'],
                                   ['установи', 'максимальную', 'насыщенность']]:
        requests.get(f'{MAIN_URL}/setSet1Max')
        res['response']['text'] = 'Готово!'
    elif get_lower_tokens(req) in [['установи', 'минимальную', 'яркость'],
                                   ['установи', 'минимальную', 'насыщенность']]:
        requests.get(f'{MAIN_URL}/setSet1Min')
        res['response']['text'] = 'Готово!'

    else:
        res['response']['text'] = 'Я не знаю, что ответить'
