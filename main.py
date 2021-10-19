import csv
import re

# читаем адресную книгу в формате CSV в список contacts_lis

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
    #pprint(contacts_list)

mymym = []
for list in contacts_list:
  for elem in list:
    mymym.append(elem)
pt = ' '.join(str(e) for e in mymym)
#print(pt)

pattern = re.compile(r'\S+@\S+')
email = pattern.findall(pt)
print(email)

patternr = re.compile(r'(\+7|8)?(\s+)*(\(\d+\))(\s*)(\d+)([\s-]*)(\d+)([\s-]*)(\d+)')
# first one (\+7|8)?\(\d+\)\s*\d+[\s-]*\d+[\s-]*\d+
#(\+7|8)?(\s+)*(\(\d+\))(\s*)(\d+)([\s-]*)(\d+)([\s-]*)(\d+)
#(\+7|8)*(\s+)*(\d+)
#\(*[доб](\.)*\s\d+\)*
phone = patternr.findall(pt)
print(phone)



patternrs2 = re.compile(r'\,*\,[А-ЯЁ-ё]+\,')
organization = patternrs2.findall(pt)
print(organization)

#r"(\w+)\s(\w+)\s(\w+)")
patternrs = re.compile(r"[А-Яа-я]{2,25}\s*( [А-Яа-я]{2,25})*\s*([А-Яа-я]{2,25})*\s*")
#(\w+)\s(\w+)\s(\w+)
name = patternrs.findall(pt)
print(name)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)


