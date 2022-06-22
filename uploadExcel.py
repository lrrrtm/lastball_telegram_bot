from constants import *
import sqlite3
from openpyxl import load_workbook
from random import randint

arr = []

wb = load_workbook('1.xlsx')
sheet = wb.get_sheet_by_name('Лист1')
db = sqlite3.connect(database, check_same_thread=False)
cur = db.cursor()

def check(cur):
    if cur not in arr:
        return True
    return False

for a in range(2, 204):
    firstname, lastname = sheet[f'B{a}'].value, sheet[f'C{a}'].value
    key = randint(100000, 999999+1)
    while check(key) != True:
        key = randint(100000, 999999+1)
    arr.append(key)
    cur.execute(f"insert into mainTable (firstname, lastname, key, status) values (\"{firstname}\", \"{lastname}\", \"Q{key}\", \"0\")")
    db.commit()