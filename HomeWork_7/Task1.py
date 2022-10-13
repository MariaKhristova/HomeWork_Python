# Создать телефонный справочник с возможностью импорта и экспорта данных в
# нескольких форматах.

import pb_export as exp
import pb_import as imp
import pb_operations as ops

phonebook = []

while True:
    print('Доступные операции: \n'
          '1) Просмотреть справочник\n'
          '2) Добавить запись\n'
          '3) Удалить запись\n'
          '4) Экспорт формат 1\n'
          '5) Импорт формат 1\n'
          '6) Экспорт формат 2\n'
          '7) Импорт формат 2\n'
          '8) Выход\n'
          )
    user_input = input("Введите номер операции: ")

    if not user_input.isdigit():
        print("Номер операции указан неверно")
        continue

    elif user_input == "1":
        ops.print_phonebook(phonebook)

    elif user_input == "2":
        ops.add_record(phonebook)

    elif user_input == "3":
        ops.delete_record(phonebook)

    elif user_input == "4":
        exp.export1(phonebook)

    elif user_input == "5":
        imp.import1(phonebook)

    elif user_input == "6":
        exp.export2(phonebook)

    elif user_input == "7":
        imp.import2(phonebook)

    elif user_input == "8":
        break

