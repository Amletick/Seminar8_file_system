from return_data_file import data_file
from rows_numeration import fix_row_numbers

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

        # Спрашиваем пользователя, нужно ли удалить скопированную строку из копируемого файла
        delete_copy_row = input("Хотите ли вы удалить скопированную строку из исходного файла? (да/нет): ").lower()
        
        if delete_copy_row == 'да':
            # Удаляем скопированную строку из копируемого файла
            del data_copy[number_row - 1]

            with open(f'db/data_{nf_copy}.txt', 'w', encoding='utf-8') as file_copy:
                file_copy.writelines(data_copy)
            # Используем функцию для коррекции номеров строк в копируемом файле
            fix_row_numbers(f'db/data_{nf_copy}.txt')
        
        with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)
        # Используем функцию для коррекции номеров строк в исходном файле
        # В принципе она не нужна, т.к копирование происходит в последнюю строку, нет смысла проверять нумерацию
        #fix_row_numbers(f'db/data_{nf}.txt')
        
        print(f"Строка успешно скопирована! Новый номер строки: {count_rows_new}")