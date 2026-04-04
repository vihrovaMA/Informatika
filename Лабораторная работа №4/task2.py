import csv   #импортируем модуль для работы с CSV файлами
import json  #импортируем модуль для работы с JSON файлами

INPUT_FILENAME = "input.csv" #задаем имя входного CSV файла
OUTPUT_FILENAME = "output.json" #задаем имя выходного JSON файла

def task() -> None: #определяем функцию, которая ничего не возвращает
    res = []  #создаем пустой список для хранения данных из CSV
    with open(INPUT_FILENAME, 'r') as file: #открываем CSV файл в режиме чтения
        read = csv.DictReader(file) #читаем CSV и преобразуем каждую строку в словарь, в котором ключи - названия столбцов
        for row in read: #перебираем каждую строку CSV файла
            res.append(row) #добавляем текущую строку в список result
    with open(OUTPUT_FILENAME, 'w') as file: #открываем JSON файл в режиме записи
        json.dump(res, file, indent=4) #записываем список словарей в JSON файл с отступами 4 пробела

if __name__ == '__main__': #проверяем, что программа запущена напрямую, а не импортирована
    task() #вызываем функцию task

    with open(OUTPUT_FILENAME) as output_f: #открываем созданный JSON файл для чтения
        for line in output_f: #перебираем файл построчно
            print(line, end="") #выводим каждую строку без добавления лишнего переноса строки