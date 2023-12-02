import random

READY_PHRASES = [
    "Готово!",
    "Сделала!",
    "Успешно!",
    "Выполнено!",
    "Завершено!",
    "Завершено успешно!",
    "Выполнено успешно!",
    "Всё готово!",
    "Миссия выполнена!",
    "Сделано!",
]

ERROR_PHRASES = [
    'Я не могу понять ваш запрос',
    'Извините, но я не распознала команду',
    'Что-то пошло не так, пожалуйста, повторите запрос',
    'Кажется, возникла проблема, попробуйте еще раз',
    'Извините, я не знаю, как на это ответить'
]


def get_lower_phrase(request) -> str:
    try:
        nlu_tokens = request['request']['nlu']['tokens']
        if len(nlu_tokens) != 0 and nlu_tokens[0].lower() == 'алиса':
            nlu_tokens = nlu_tokens[1:]
        return ' '.join([x.lower() for x in nlu_tokens])
    except KeyError:
        print('Error: Missing key in the request object.')
        return ''
    except TypeError:
        print('Error: Invalid request object type.')
        return ''


def get_lower_tokens(request) -> [str]:
    try:
        nlu_tokens = request['request']['nlu']['tokens']
        if len(nlu_tokens) != 0 and nlu_tokens[0].lower() == "алиса":
            nlu_tokens = nlu_tokens[1:]
        return [x.lower() for x in nlu_tokens]
    except KeyError:
        print("Error: Missing key in the request object.")
        return []
    except TypeError:
        print("Error: Invalid request object type.")
        return []


def get_ready_phrase():
    return random.choice(READY_PHRASES)


def get_error_phrase():
    return random.choice(ERROR_PHRASES)
