
import sqlite3

conn = sqlite3.connect(emaildb.sqlite)#If dont exist it will create one
cur = conn.cursor() #create a objecto to interact with db

cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1) fname = 'mbox-shor.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('''SELECT FROM Counts WHERE email = ?''',(email,))#? act as a place holder that filled with tuple in this case (email,)
    row = cur.fetchone() #read just one row, the first row
    if row is None:
        cur.execute('''INSERT INTO Counts (email,count) VALUES (?, 1)''', (email,))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE email = ?''', (email,))
    conn.commit #commit changes from object created by python to real db

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close() ##Close connection with db