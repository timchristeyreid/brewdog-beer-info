import json
import sqlite3

conn = sqlite3.connect('beers.db')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Beer;

CREATE TABLE Beer (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    tagline TEXT UNIQUE,
    abv INTEGER
);

''')

with open('beers.json', 'r') as openfile:
    data = json.load(openfile)

for item in data:
    name = item['name']
    tagline = item['tagline']
    abv = item['abv']

    cur.execute('''INSERT OR REPLACE INTO Beer
        (name, tagline, abv) VALUES ( ?, ?, ? )''',
        ( name, tagline, abv ) )

    conn.commit()