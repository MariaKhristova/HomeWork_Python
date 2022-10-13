def export_data(phonebook: list, delimiter: str):
    name = input("Введите название файла : ")
    f = open(name, "wb")
    for record in phonebook:
        record_str = f'{record["Фамилия"]}{delimiter}{record["Имя"]}{delimiter}{record["Телефон"]}{delimiter}{record["Описание"]}\n\n'
        f.write(record_str.encode("utf8"))
    f.close()


def export1(phonebook):
    delimiter = '\n'
    export_data(phonebook, delimiter)


def export2(phonebook):
    delimiter = ','
    export_data(phonebook, delimiter)
