list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины находим путем расчета количества игроков в списке и последующим делением его на два
middle_index = len(list_players) // 2
# путем слайсирования делим игроков на две равные команды
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(first_team) #вывод первой команды участников
print(second_team) #вывод второй команды участников
