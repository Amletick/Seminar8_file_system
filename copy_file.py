from choice_file import choice_number_file
from return_data_file import data_file

def copy_file():
    print("Выберите файл, в который вы хотите скопировать данные")
    data, nf = data_file()
    print("Выберите файл, из которого вы хотите скопировать данные")
    data_copy, nf_copy = data_file()

    # Проверяем не пуст ли копируемый файл
    count_rows = len(data_copy)
    if count_rows == 0:
        print("Копируемый файл пустой!")
    else:
        # Выбираем строку для копирования
        number_row = int(input(f"Введите номер строки для копирования "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка! "
                                   f"Введите номер строки для копирования "
                                   f"от 1 до {count_rows}: "))

        # Запоминаем выбранную строку и добавляем её в конец исходного файла
        copy_row = data_copy[number_row - 1]
        data.append(copy_row)
        
        # Пересчитываем количество строк после добавления
        count_rows_new = len(data)
        
        # Обновляем номер строки в самом файле
        data[-1] = f"{count_rows_new};{';'.join(copy_row.split(';')[1:])}"

        with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)
        
        print(f"Строка успешно скопирована! Новый номер строки: {count_rows_new}")
