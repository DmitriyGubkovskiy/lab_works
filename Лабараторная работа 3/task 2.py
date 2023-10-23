# TODO Напишите функцию find_common_participants
def find_common_participants(s1, s2, c=","):
    s1 = s1.split(c)
    s2 = s2.split(c)
    return sorted(set(s1).intersection(s2))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
