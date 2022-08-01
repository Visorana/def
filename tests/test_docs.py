import unittest
from main import UserCommands
from unittest.mock import patch


class TestGetName(unittest.TestCase):

    @patch('builtins.input', side_effect=['p', '11-2'])
    def test_got_name(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Геннадий Покемонов')

    @patch('builtins.input', side_effect=['p', '1164'])
    def test_no_name(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Документ не найден.')

    @patch('builtins.input', side_effect=['p', '11-2'])
    @unittest.expectedFailure
    def test_failure(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Аристарх Павлов')


class TestGetNameShelf(unittest.TestCase):

    @patch('builtins.input', side_effect=['s', '10006'])
    def test_got_shelf(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Полка 2.')

    @patch('builtins.input', side_effect=['s', '34-78'])
    def test_no_shelf(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Несуществующий номер документа.')

    @patch('builtins.input', side_effect=['s', '2207 876234'])
    @unittest.expectedFailure
    def test_failure(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Полка 2.')


class TestGetList(unittest.TestCase):

    @patch('builtins.input', return_value='l')
    def test_got_list(self, mock_input):
        self.assertEqual(UserCommands().user_choice(), 'passport, 2207 876234, Василий Гупкин\n'
                                                       'invoice, 11-2, Геннадий Покемонов\n'
                                                       'insurance, 10006, Аристарх Павлов\n')

    @patch('builtins.input', return_value='l')
    @unittest.expectedFailure
    def test_failure(self, mock_input):
        self.assertEqual(UserCommands().user_choice(), 'passport, 2207 876234, Василий Гупкин\n'
                                                       'invoice, 11-2, Геннадий Покемонов\n')


class TestAddDoc(unittest.TestCase):

    @patch('builtins.input', side_effect=['a', 'passport', '123', 'John Smith', '3'])
    def test_added_doc(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Новый документ добавлен.')

    @patch('builtins.input', side_effect=['a', 'passport', '123', 'John Smith', '4'])
    def test_no_shelf(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Несуществующий номер полки. Доступные полки: 1, 2, 3')

    @patch('builtins.input', side_effect=['a', 'passport', '123', 'John Smith', '3'])
    @unittest.expectedFailure
    def test_failure(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Несуществующий номер полки. Доступные полки: 1, 2, 3')


class TestDelDoc(unittest.TestCase):

    @patch('builtins.input', side_effect=['d', '2207 876234'])
    def test_deleted_doc(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Документ удалён.')

    @patch('builtins.input', side_effect=['d', '123'])
    def test_no_doc(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Несуществующий номер документа.')

    @patch('builtins.input', side_effect=['d', '123'])
    @unittest.expectedFailure
    def test_failure(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Документ удалён.')


class TestMoveDoc(unittest.TestCase):

    @patch('builtins.input', side_effect=['m', '2207 876234', '3'])
    def test_moved_doc(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Документ перемещён.')

    @patch('builtins.input', side_effect=['m', '2207 876234', '4'])
    def test_no_shelf(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Полка не найдена.')

    @patch('builtins.input', side_effect=['m', '123'])
    def test_no_doc(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Документ не найден.')

    @patch('builtins.input', side_effect=['m', '2207 876234', '4'])
    @unittest.expectedFailure
    def test_failure(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Документ перемещён.')


class TestAddShelf(unittest.TestCase):

    @patch('builtins.input', side_effect=['as', '4'])
    def test_shelf_added(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Полка добавлена.')

    @patch('builtins.input', side_effect=['as', '3'])
    def test_shelf_exists(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Полка уже существует.')

    @patch('builtins.input', side_effect=['as', '3'])
    @unittest.expectedFailure
    def test_failure(self, mock_inputs):
        self.assertEqual(UserCommands().user_choice(), 'Полка добавлена.')
