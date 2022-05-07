# to get the current date
from datetime import date

today = str(date.today()).split('-')
# tday = str(today).split('-')
print(int(today[0]))
# dd/mm/YY
# d1 = today.strftime("%d/%m/%Y")
# print("d1 =", d1)
