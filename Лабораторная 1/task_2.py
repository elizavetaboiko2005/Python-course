# TODO Найдите количество книг, которое можно разместить на дискете

storage = 1.44 # Информационный объем в Мб
pages_in_book = 100
lines_per_page = 50
symbols_per_line = 25
storage_per_symbol = 4 # Объем в байтах

storage_in_bites = storage * 1024 * 1024
symbols_in_book = symbols_per_line * lines_per_page * pages_in_book
storage_for_book = storage_per_symbol * symbols_in_book
number_of_books = storage_in_bites // storage_for_book

print("Количество книг, помещающихся на дискету:", round(number_of_books))
