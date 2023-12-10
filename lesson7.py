with open ('airport-codes_csv.csv', 'r',encoding='utf-8') as file:
    file_content = file.readlines()
    for line in file_content:
        if line.split(';')[5] == 'UA': print(line.split(';')[2])
