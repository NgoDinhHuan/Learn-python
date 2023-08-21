import sys
import os
import sqlite3


conn = sqlite3.connect("demo.db")

cur = conn.cursor()


data = [
    (7,'AAAAAA','020202020202'),
    (8,'BBBBB','121212212'),
    (9,'CCCCC','459825623660'),
]
cur.executemany("INSERT OR IGNORE INTO sinhvien VALUES(?, ?, ?)",data)
conn.commit()
conn.close()