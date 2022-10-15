import os.path
import json

file_name = 'company.json'
company_as_dict = [{"id": 1, "FirstName": "FirstName", "Position": "Position", "Salary": 1}]


def read_json():
    if not os.path.isfile(file_name):
        print(f'Файл не существует {file_name}')
        with open(file_name, 'w') as f:
            json.dump(company_as_dict, f)
    with open(file_name, 'r') as f:
        data = json.load(f)
        company_as_dict.clear()
        company_as_dict.extend(data)


def save_json():
    with open(file_name, 'w') as f:
        json.dump(company_as_dict, f)
    print('Файл сохранен')


def find_person(emp_id):
    for emp in company_as_dict:
        if emp['id'] == emp_id:
            return emp
    return None


def add_employer(emp_as_dict):
    company_as_dict.append(emp_as_dict)


def remove_employer(employer_id):
    for emp in company_as_dict:
        if emp['id'] == employer_id:
            company_as_dict.remove(emp)
