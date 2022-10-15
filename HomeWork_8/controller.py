import model
import view_person


def main():
    model.read_json()
    while True:
        action = view_person.view_menu()
        if action == '1':  # добавить сотрудника
            employer = view_person.get_new_employer()
            model.add_employer(employer)

        if action == '2':  # найти сотрудника
            employer_id = int(view_person.find_employer())
            employer = model.find_person(employer_id)
            view_person.print_employer(employer)

        if action == '3':  # просмотреть список сотрудников
            view_person.print_employers(model.company_as_dict)

        if action == '4':  # удалить сотрудника
            employer_id = int(view_person.find_employer())
            model.remove_employer(employer_id)

        if action == '5':  # сохранить в файл
            model.save_json()

        if action == '6':  # Загрузить из файла
            model.read_json()

        if action == 'q':  # завершение работы
            save = view_person.save_question()
            if save:
                model.save_json()
            break
