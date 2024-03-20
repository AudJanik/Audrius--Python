import os
import sqlite3
from rde_sukos import istraukti_produktus

def create_db():
    conn = sqlite3.connect('produktai.db')
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS produktai(
    id INTEGER PRIMARY KEY,
    pavadinimas text,
    kaina text,
    kiekis int)''')

    conn.commit()
    conn.close()

def prideti_produkta(produktai):
    conn = sqlite3.connect('produktai.db')
    c = conn.cursor()
    for produktas in produktai:
        c.execute('INSERT INTO produktai (pavadinimas, kaina, kiekis) VALUES (?,?,?)',
              (produktas['pavadinimas'], produktas['kaina'], produktas['kiekis']))

    conn.commit()
    conn.close()

def gauti_produktus():
    conn = sqlite3.connect('produktai.db')
    c = conn.cursor()
    c.execute('SELECT * FROM produktai')
    produktai = c.fetchall()
    conn.close()
    return produktai

produktai = istraukti_produktus('https://www.rde.lt/categories/lt/277/sort/5/filter/0_0_0_0/page/1/Plauk%C5%B3-formavimo-%C5%A1ukos.html')
create_db()
prideti_produkta(produktai)