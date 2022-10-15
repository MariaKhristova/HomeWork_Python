def view_menu():
    print('Доступные операции: \n'
          '1) Добавить сотрудника\n'
          '2) Найти сотрудника\n'
          '3) Просмотреть список сотрудников\n'
          '4) Удалить сотрудника\n'
          '5) Сохранить в файл\n'
          '6) Загрузить из файла\n'
          'q) Завершение работы\n'
          )
    action = input('Укажите выбор: ')
    return action


def get_emp_info(info_type):
    data = input(f'Введите {info_type}: ')
    return data


def get_new_employer():
    emp_id = int(get_emp_info('ИД'))
    first_name = get_emp_info('ФИО')
    position = get_emp_info('Должность')
    salary = int(get_emp_info('Зарплата'))
    emp_as_dict = {"id": emp_id, "FirstName": first_name, "Position": position, "Salary": salary}
    return emp_as_dict


def save_question():
    data = input('Желаете сохранить данные перед выходом? (y/n):')
    if (data == 'y'):
        return True
    return False


def find_employer():
    data = input('Введите ИД сотрудника: ')
    return data


def print_employer(employer):
    print(employer)


def print_employers(company_as_dict):
    print(company_as_dict)
