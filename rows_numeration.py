def fix_row_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Пересчитываем номера строк
    for i in range(len(lines)):
        parts = lines[i].split(';')
        correct_number = str(i + 1)
        if parts[0] != correct_number:
            parts[0] = correct_number
            lines[i] = ';'.join(parts)

    # Записываем обновленные строки обратно в файл
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)