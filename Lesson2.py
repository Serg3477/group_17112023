name = "Alex "

surname = "Clinton"

reaction = "\U00002601"

# full_name = name + surname
full_name = f"{name}{surname}"
print(full_name)
print(reaction)

another_string = "    dfghsrhg  hfjkfhjk"
no_whitespaces = another_string.strip()
print(no_whitespaces)

print("*" * 20)

another_string = "5"

# poem = """
# Як умру то поховайте
# мене на могилі
# """
poem = "Як умру ещ поховайте\n мене на могили"
print(poem)
print(poem, another_string, sep="_______", end="***")

another_string = "  \n   \t   dfghsrhg  hfjkfhjk"
print(another_string)

sity = "odesa"
sity = sity.strip().title()
print(sity)

some_string = "56565657"
print(some_string.isdigit())
some_string = "565656~"
proc_string = some_string.strip("~")
print(proc_string.isdigit())

print(len(some_string))

some_string = "56565657"
print(some_string.count("6"))
print(ord("+"))
print(chr(57))

print("aa" + "A")

print(some_string.startswith("56"))
print(some_string.endswith("7"))

price = 2000
quantity = 100
total = price * quantity
print(total)
# print(f"{total}")
insurance_rate = 0.05
print(insurance_rate)
ins_per_car = insurance_rate * price
print(ins_per_car)
strange_number = 0.1 + 1.2
print(round(strange_number))

print(101 % 50)
print(100 // 30)
print(2**2)






