# brings in needed tools
from datetime import datetime
import sqlite3



# creates new sql file, sets up cursor tool, gets rid of old tables, creates desired table
conn = sqlite3.connect('toyotadb.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Down_Days;

CREATE TABLE Down_Days(
    pct_change REAL,
    volume INTEGER,
    day DATE
)
''')

# brings in file, opens it, strips
f = input("Enter file:")
file = open(f)
for line in file:
    line = line.strip()
# protects against errors
    if not line:
        continue
# protects against errors
    words = line.split(",")
    if len(words) < 6:
        continue
# protects against errors
    if words[0] == "Date":
        continue
# finds desried pieces of data
    open_price = float(words[4])
    close_price = float(words[1])
    volume = int(words[5])
    pct_change = ((close_price - open_price) / open_price)
    if pct_change >= 0:
        continue
    day = words[0]

# putting the data into  table in sql
    cur.execute("INSERT INTO Down_Days (pct_change, volume, day) VALUES (?,?,?)", (pct_change, volume, day))

# create new desired table w/ edits
query = "SELECT pct_change, volume, day FROM Down_Days ORDER BY pct_change LIMIT 20"
cur.execute(query)
Sorted_Down_Days = cur.fetchall()

# formats how data table should show in python
print(f"{'pct_change': ^22} | {'volume': ^22} | {'day': ^22}")
print("-"*70)
for pct_change, volume, day in Sorted_Down_Days:
    print(f"{pct_change:^22.2%} {volume:^24} {day:^26}")
        
conn.commit()
conn.close()


    

    



