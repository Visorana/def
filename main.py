documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def main():
    print('Пользовательские команды:',
          'p - узнать имя человека по номеру документа.',
          's - номер полки, где находится документ.',
          'l - вывести список всех документов.',
          'a - добавить новый документ.',
          'd - удалить документ по номеру.',
          'm - переместить документ на другую полку по номеру.',
          'as - добавить новую полку.', sep='\n')
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            get_name()
        elif user_input == 's':
            get_shelf()
        elif user_input == 'l':
            get_list_of_docs()
        elif user_input == 'a':
            add_new_doc()
        elif user_input == 'd':
            del_doc()
        elif user_input == 'm':
            trans_doc()
        elif user_input == 'as':
            add_shelf()
        else:
            print('Несуществующая команда.')


def is_valid(id_number):
    for i in documents:
        if id_number == i['number']:
            return True
    else:
        return False


def is_available(id_number):
    return id_number in sum(directories.values(), [])


def get_name():
    while True:
        id_number = input('Введите номер документа: ')
        if is_valid(id_number):
            for i in documents:
                if id_number == i['number']:
                    print(i['name'], '', sep='\n')
                    return
        else:
            print('Несуществующий номер документа.')


def get_shelf():
    while True:
        id_number = input('Введите номер документа: ')
        if is_available(id_number):
            for shelf in directories:
                if id_number in directories[shelf]:
                    print(f'Полка {shelf}.', '', sep='\n')
                    return
        else:
            print('Несуществующий номер документа.')


def get_list_of_docs():
    for person in documents:
        print(f"{person['type']} \"{person['number']}\" \"{person['name']}\"")
    print()
    return


def add_new_doc():
    new_doc = dict(type=input('Тип документа: '), number=input('Номер документа: '), name=input('Имя: '))
    while True:
        s_number = input('Номер полки для документа: ')
        if s_number in directories:
            documents.append(new_doc)
            directories[s_number].append(documents[-1]['number'])
            print('Новый документ добавлен.', '', sep='\n')
            return
        else:
            print('Несуществующий номер полки. Доступные полки:', ', '.join(directories.keys()))


def del_doc():
    while True:
        id_number = input('Введите номер документа: ')
        if is_valid(id_number):
            for person in documents:
                if id_number == person['number']:
                    del documents[documents.index(person)]
                    continue
            for shelf in directories:
                if id_number in directories[shelf]:
                    del directories[shelf][directories[shelf].index(id_number)]
                    print('Документ удалён.', '', sep='\n')
                    return
        else:
            print('Несуществующий номер документа.')


def trans_doc():
    while True:
        id_number = input('Введите номер документа: ')
        if is_available(id_number):
            while True:
                s_number = input('Введите номер полки для перемещения: ')
                if s_number in directories.keys():
                    for shelf in directories.values():
                        if id_number in shelf:
                            directories[s_number].append(shelf.pop(shelf.index(id_number)))
                            print('Документ перемещён.', '', sep='\n')
                            return
                else:
                    print('Несуществующий номер полки. Доступные полки:', ', '.join(directories.keys()))
        else:
            print('Несуществующий номер документа.')


def add_shelf():
    while True:
        s_number = input('Номер новой полки: ')
        if s_number in directories:
            print('Полка уже существует.')
        else:
            directories[s_number] = []
            print('Полка добавлена.', '', sep='\n')
            return


main()
