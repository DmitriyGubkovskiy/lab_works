# TODO Найдите количество книг, которое можно разместить на дискете

information_capacity = 1.44
delta = 1024  # переменная для перевода в байты (без какой-либо магии)
page_count = 100
string_count = 50
symbol_count = 25
capacity_symbol = 4
res = (information_capacity * delta * delta) // (page_count * string_count * symbol_count * capacity_symbol)
print("Количество книг, помещающихся на дискету:", int(res))
