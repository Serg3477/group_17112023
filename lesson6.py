import requests
url = "https://script.googleusercontent.com/macros/echo?user_content_key=nQFmR2vM4xH4Na_Y5j-fi5Wfg86MNIMM2s87NVDxnQxz4ZCROsdD9ljDm0mrd7Yzt95_vbT5CyR_RXOFKkONsipW7ky6U2ftm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnOJBD_zxFgzsPlOsKAjD7MWea3fhzz77L0yQlA2tADhxhvMNJnbDfw_1-ZmA-wRTgsPzMzCaG9jKrx_J0zXRt0jyn1Z4YyOlLg&lib=M1Q6pRfSm0559Ga_BuYfp8eoySTrMnX_x"
response = requests.get(url = url)
data_from_net = response.json()
id_people = data_from_net['people']
large_family_count = 0
deptor_family = 0
woman_with_home = 0
for key in id_people:
    if (key['age'] >= 35  and key['large_family']):
        print(str(key['name']) + " " + str(key['age']) + " років, багатодітна сім'я. Місячний дохід становить: " + str(key['salary']))
        print("*" * 50)
    if (key['large_family']): large_family_count += 1
    if ((key['loan_costs']) > (key['salary'])): deptor_family += 1
    if str(key['gender']) == "жінка " and key['home_owner']: woman_with_home += 1
print("Кількість багатодітних сімей: " + str(large_family_count))
print("Кількість сімей, в яких витрати за кредитами більші за доходи: " + str(deptor_family))
print("Кількість жінок, які забезпечені власним житлом: " + str(woman_with_home))

