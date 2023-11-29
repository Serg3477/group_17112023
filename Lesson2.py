print("*" * 40)
print ("Введідь ваше ім'я: ")
name = input ()
print ("Введіть ваш вік: ")
age = input()
print("Введіть значення вашої місячної заробітної плати на даний момент: ")
salary = input()
leftover = (65 - int(age))
leftover_month = (leftover * 12)
total_salary = float(salary) * leftover_month
dollar_rate = 37.3
convert_salary = total_salary / dollar_rate
toyota_price = 31500
toyota_quantity = (convert_salary / toyota_price)
full_text = ("Я, " + (name) + ", зможу заробити лише__" + str(round(convert_salary, 2)) + "__доларів, \n що вистачить лише на__" + str(round(toyota_quantity)) + "__тойот, мене це не влаштовує, тому я буду змінювати своє життя\n і буду завзято вивчати програмування")
print(full_text)














