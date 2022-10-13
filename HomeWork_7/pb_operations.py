
def print_phonebook(phonebook):
    if len(phonebook) == 0:
        print('Справочник пуст')
        return
    formatted = '\n'.join([f'{i + 1}) {x["Фамилия"]}, {x["Имя"]}, {x["Телефон"]}, {x["Описание"]}' for i, x in enumerate(phonebook)])
    print(formatted)


def add_record(phonebook: list):
    while True:
        data = input("Введите через запятую данные Фамилия, Имя, Телефон, Описание или q для отмены: ")
        if data.lower() == 'q':
            return
        data_arr = [x.strip() for x in data.split(',')]
        if len(data_arr) != 4:
            print("Некорректный ввод данных")
            continue
        break
    phonebook.append({'Фамилия': data_arr[0], 'Имя': data_arr[1], 'Телефон': data_arr[2], 'Описание': data_arr[3]})


def delete_record(phonebook: list):
    if len(phonebook) == 0:
        print('Справочник пуст')
    while True:
        data = input("Введите номер записи для удаления или q для отмены: ")
        if data.lower() == 'q':
            return

        if not data.isnumeric():
            print("Некорректный ввод данных")
            continue

        index = int(data)
        if len(phonebook) < index:
            print(f'Запись под номером {index} не существует')
            continue

        break
    del(phonebook[index - 1])
