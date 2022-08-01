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


class UserCommands:

    def __init__(self):
        self.input_dict = {'p': self.get_name, 's': self.get_shelf, 'l': self.get_list,
                           'a': self.add_doc, 'd': self.del_doc, 'm': self.move_doc, 'as': self.add_shelf}

    @staticmethod
    def get_name():
        id_number = input('Введите номер документа: ')
        for i in documents:
            if id_number == i['number']:
                return i['name']
        return 'Документ не найден.'

    @staticmethod
    def get_shelf():
        id_number = input('Введите номер документа: ')
        for shelf in directories:
            if id_number in directories[shelf]:
                return f'Полка {shelf}.'
        return 'Несуществующий номер документа.'

    @staticmethod
    def get_list():
        res = ''
        for person in documents:
            res += f"{person['type']}, {person['number']}, {person['name']}\n"
        return res

    @staticmethod
    def add_doc():
        new_doc = dict(type=input('Тип документа: '), number=input('Номер документа: '), name=input('Имя: '))
        shelf_number = input('Номер полки для документа: ')
        if shelf_number in directories:
            print(type(directories))
            documents.append(new_doc)
            directories[shelf_number].append(new_doc['number'])
            return 'Новый документ добавлен.'
        else:
            return f"Несуществующий номер полки. Доступные полки: {', '.join(directories.keys())}"

    @staticmethod
    def del_doc():
        id_number = input('Введите номер документа: ')
        for person in documents:
            if id_number == person['number']:
                del documents[documents.index(person)]
        for shelf in directories:
            if id_number in directories[shelf]:
                directories[shelf].remove(id_number)
                return 'Документ удалён.'
        return 'Несуществующий номер документа.'

    @staticmethod
    def move_doc():
        id_number = input('Введите номер документа, который хотите переместить: ')
        if id_number in sum(directories.values(), []):
            number_shelf = input('Введите номер полки, на которую хотите переместить документ: ')
            if number_shelf not in directories:
                return 'Полка не найдена.'
            for shelf, value in directories.items():
                if id_number in value:
                    directories[number_shelf] += [id_number]
                    value.remove(id_number)
                    return 'Документ перемещён.'
        return 'Документ не найден.'

    @staticmethod
    def add_shelf():
        shelf_number = input('Номер новой полки: ')
        if shelf_number in directories:
            return 'Полка уже существует.'
        else:
            directories[shelf_number] = []
            return 'Полка добавлена.'

    def user_choice(self):
        print('Пользовательские команды:\n'
              'p - узнать имя человека по номеру документа.\n'
              's - номер полки, где находится документ.\n'
              'l - вывести список всех документов.\n'
              'a - добавить новый документ.\n'
              'd - удалить документ по номеру.\n'
              'm - переместить документ на другую полку по номеру.\n'
              'as - добавить новую полку.')
        choice = input('\nВведите команду: ').lower()
        if choice in self.input_dict.keys():
            return self.input_dict[choice]()
        else:
            return 'Команда не найдена.'


if __name__ == '__main__':
    result = UserCommands().user_choice()
    print(result)

