cities_visited = input("Введіть назви міст, в яких ви побували (через пробіл): ")
list_cities_visited = set(cities_visited.title().split())
cities_want_to_visit = input("Введіть міста, в яких ви хотіли б побувати (через пробіл): ")
list_cities_want_to_visit = set(cities_want_to_visit.title().split())
list_cities_already_visited = list_cities_visited & list_cities_want_to_visit
if list_cities_already_visited:
    print(f'Вам мабудь сподобалося в містах {list_cities_already_visited}. Тому ви хотіли б побувати там знову.')
else: print ("Ви відкриті до чогось нового!")


