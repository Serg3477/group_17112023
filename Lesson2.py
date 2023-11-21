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

print(some_string.startswith(56))
print(some_string.endswith(7))

age = 15
print(age)


