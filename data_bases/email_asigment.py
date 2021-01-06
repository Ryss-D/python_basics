
import sqlite3
import urllib.request, urllib.parse, urllib.error


conn = sqlite3.connect('email_asigment.sqlite')#If dont exist it will create one
cur = conn.cursor() #create a objecto to interact with db

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

# fhand = urllib.request.urlopen('https://www.py4e.com/code3/mbox.txt')
# fh = fhand.read()
# print(fh) idk why its forbidden
fh = open('C:\projects\python\data_bases\mbox.txt')

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    places = email.split('@')
    org = places[1]
    cur.execute('''SELECT * FROM Counts WHERE org = ?''',(org,))#? act as a place holder that filled with tuple in this case (email,)
    row = cur.fetchone() #read just one row, the first row
    if row is None:
        cur.execute('''INSERT INTO Counts (org,count) VALUES (?, 1)''', (org,))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''', (org,))
conn.commit() #commit changes from object created by python to real db

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close() ##Close connection with db