sentence = "6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$"
cities = sentence.split()
city1_1 = list(cities[0])
city1_2 = city1_1[5:9]
string = ""
for element in city1_2:
    string += element 
cities[0] = string
element = 0
string = ""

city6_1 = list(cities[6])
city6_2 = city6_1[:8]
for element in city6_2:
    string += element 
cities[6] = string
string = "Я " + "\U00002764 "


for i in range(6):
    lowercase = cities[int(i)].lower()
    upper_first = lowercase.title() 
    string = "Я " + "\U00002764 "
    print(string + upper_first)
