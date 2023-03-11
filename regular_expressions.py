import csv
import re


def read_file(file_name):
    with open(file_name) as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


'''1. Корректировка ФИО'''


def correct_name(contacts_list):
    pattern1 = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    pattern2 = r'\1\3\10\4\6\9\7\8'
    new_list = list()
    for name in contacts_list:
        string_name = ','.join(name)
        sub_name = re.sub(pattern1, pattern2, string_name)
        split_name = sub_name.split(',')
        new_list.append(split_name)
    return new_list


'''2. Корректируем номер телефона'''


def correct_number(contacts_list):
    pattern3 = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})'\
            r'(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    pattern4 = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    new_list = list()
    for number in contacts_list:
        string_number = ','.join(number)
        sub_number = re.sub(pattern3, pattern4, string_number)
        split_number = sub_number.split(',')
        new_list.append(split_number)
    return new_list


'''Объединение дублей'''


def duplicates(contacts_list):
    for item in contacts_list:
        first_name = item[0]
        last_name = item[1]
        for element in contacts_list:
            new_first_name = element[0]
            new_last_name = element[1]
            if first_name == new_first_name and last_name == new_last_name and item is not element:
                if item[2] == '':
                    item[2] = element[2]
                if item[3] == '':
                    item[3] = element[3]
                if item[4] == '':
                    item[4] = element[4]
                if item[5] == '':
                    item[5] = element[5]
                if item[6] == '':
                    item[6] = element[6]
        new_list = list()
        for artifact in contacts_list:
            if artifact not in new_list:
                new_list.append(artifact)
        return new_list


def write_file(contacts_list):
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


if __name__ == '__main__':
    result = read_file('phonebook_raw.csv')
    result = correct_name(result)
    result = correct_number(result)
    result = duplicates(result)
    write_file(result)
