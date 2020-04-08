import json
from datetime import datetime
import data


def logger(old_function):
    def result_function(*args, **kwargs):
        today = datetime.now()
        result = old_function(*args, **kwargs)
        result = {'Дата вызова': str(today), 'Имя функции': old_function.__name__, 'Аргументы': [ args, kwargs ],
                  'Возвращаемое значение': result}
        with open(kwargs[ 'path' ], 'w', encoding='utf-8') as f:
            f.write(json.dumps(result, indent=1, ensure_ascii=False))
        return result

    return result_function


@logger
def move_document(directories, path):
    success = False
    doc_number = input("Введите номер документа: ")
    dir_requested = input("На какую полку переместить? ")
    for directory in directories:
        if doc_number in directories[ directory ] and dir_requested in directories:
            directories[ directory ].remove(doc_number)
            directories[ dir_requested ].append(doc_number)
            success = True
    if not success:
        return 'Ошибка! документ или полка отсутствует.'
    else:
        return directories


if __name__ == '__main__':
    move_document(data.directories, path='log.json')
