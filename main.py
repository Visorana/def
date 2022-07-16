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


def get_name():
    id_number = input('Введите номер документа: ')
    for i in documents:
        if id_number == i['number']:
            print(i['name'])
            return
    print('Документ не найден.')


def get_shelf():
    id_number = input('Введите номер документа: ')
    for shelf in directories:
        if id_number in directories[shelf]:
            print(f'Полка {shelf}.')
            return
    print('Несуществующий номер документа.')


def get_list():
    for person in documents:
        print(f"{person['type']} \"{person['number']}\" \"{person['name']}\"")
    print()
    return


def add_doc():
    new_doc = dict(type=input('Тип документа: '), number=input('Номер документа: '), name=input('Имя: '))
    while True:
        shelf_number = input('Номер полки для документа: ')
        if shelf_number in directories:
            documents.append(new_doc)
            directories[shelf_number].append(new_doc['number'])
            print('Новый документ добавлен.')
            return
        print('Несуществующий номер полки. Доступные полки:', ', '.join(directories.keys()))


def del_doc():
    id_number = input('Введите номер документа: ')
    for person in documents:
        if id_number == person['number']:
            del documents[documents.index(person)]
    for shelf in directories:
        if id_number in directories[shelf]:
            directories[shelf].remove(id_number)
            print('Документ удалён.')
            return
    print('Несуществующий номер документа.')


def move_doc():
    id_number = input('Введите номер документа, который хотите переместить: ')
    if id_number in sum(directories.values(), []):
        number_shelf = input('Введите номер полки, на которую хотите переместить документ: ')
        if number_shelf not in directories:
            print('Полка не найдена.')
            return
        for shelf, value in directories.items():
            if id_number in value:
                directories[number_shelf] += [id_number]
                value.remove(id_number)
                print('Документ перемещён.')
                return
    print('Документ не найден.')


def add_shelf():
    shelf_number = input('Номер новой полки: ')
    if shelf_number in directories:
        print('Полка уже существует.')
    else:
        directories[shelf_number] = []
        print('Полка добавлена.')
        return


inputDict = {'p': get_name, 's': get_shelf, 'l': get_list, 'a': add_doc, 'd': del_doc, 'm': move_doc, 'as': add_shelf}


def user_choice():
    print('Пользовательские команды:',
          'p - узнать имя человека по номеру документа.',
          's - номер полки, где находится документ.',
          'l - вывести список всех документов.',
          'a - добавить новый документ.',
          'd - удалить документ по номеру.',
          'm - переместить документ на другую полку по номеру.',
          'as - добавить новую полку.',
          'q - выход', sep='\n')
    while True:
        choice = input('Введите команду: ').lower()
        if choice == 'q':
            print('Вы вышли из программы.')
            return
        elif choice in inputDict.keys():
            inputDict[choice]()
        else:
            print('Команда не найдена.')


user_choice()

