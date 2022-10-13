def import_data(phonebook: list, delimiter: str):
    name = input("Введите название файла : ")
    f = open(name, "rb")
    data = f.read()
    f.close()
    records = list(filter(lambda x: x != '', data.decode("utf8").split('\n\n')))
    phonebook.clear()
    for record_str in records:
        data_arr = record_str.split(delimiter)
        phonebook.append({'Фамилия': data_arr[0], 'Имя': data_arr[1], 'Телефон': data_arr[2], 'Описание': data_arr[3]})


def import1(phonebook):
    delimiter = '\n'
    import_data(phonebook, delimiter)

def import2(phonebook):
    delimiter = ','
    import_data(phonebook, delimiter)
