from api_request import send_request
from utils.utils import get_lower_tokens


def handle_color(req, res, main_url):
    colors = {
        'красный': 'red',
        'ораньжевый': 'orange',
        'желтый': 'yellow',
        'зелёный': 'green',
        'голубой': 'cyan',
        'синий': 'blue',
        'фиолетовый': 'violet',
        'розовый': 'pink'
    }

    nlu_tokens = get_lower_tokens(req)
    if len(nlu_tokens) != 3 or not nlu_tokens[1] in colors:
        return

    if nlu_tokens[0] == 'установи' and nlu_tokens[2] == 'цвет':
        res['response']['text'] = send_request(f'{main_url}/color/set?color={colors[nlu_tokens[1]]}')
        return True
