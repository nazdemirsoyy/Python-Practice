import sqlite3

conn = sqlite3.connect('/Users/naz.demirsoy/Documents/python/Tracks/trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''    
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

file_path = '/Users/naz.demirsoy/Documents/python/Tracks/tracks.csv'

try:
    handle = open(file_path)
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit()

for line in handle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 6: 
        continue  # Skip malformed lines

    name, artist, album, count, rating, length = pieces[:6]


    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    genre_name = 'Rock'  # Default genre
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre_name,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre_name,))
    genre_id = cur.fetchone()[0]


    cur.execute('''
        INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)''', (name, album_id, genre_id, length, rating, count))


conn.commit()
handle.close()

#Test
print("Verifying data in the database...")
for row in cur.execute('SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre ON Track.genre_id = Genre.id JOIN Album ON Track.album_id = Album.id JOIN Artist ON Album.artist_id = Artist.id ORDER BY Artist.name LIMIT 5'):
    print(row)

conn.close()
