from dialog_handler import handle_dialog

MAIN_URL = 'https://bbasv16cnlinufmp5h8j.containers.yandexcloud.net'


def main(event, context):
    response = {
        'session': event['session'],
        'version': event['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(event, response, MAIN_URL)
    return response