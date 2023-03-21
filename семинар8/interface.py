from input_data import *
from output_data import *

def StartMenu():
    print('\nТелефонный справочник. Выберите действие:\n')
    print('1 - добавить в справочник')
    print('2 - вывести всех')
    print('3 - поиск по имени')
    print('4 - изменение записи')
    print('5 - удаление записи')
    print('6 - выход')

    choice = int(input())
    match choice:
        case 1:
            AddData(input('Введите имя:\t'), input('Введите номер:\t'))
            return True
        case 2:
            ShowAll()
            return True
        case 3:
            Search(input('Введите имя:\t'))
            return True
        case 4:
            ChangeData(input('Введите старое имя:\t'), input('Введите новое имя:\t'), input('Введите новый номер:\t'))  
            return True
        case 5:
            DeleteData(input('Введите удаляемое имя:\t'), input('Введите удаляемый номер:\t'))  
            return True 
        case 6:
            return False


        