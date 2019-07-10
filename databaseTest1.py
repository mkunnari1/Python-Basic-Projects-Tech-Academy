

import sqlite3


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("create table if not exists tbl_persons(\
        ID integer primary key autoincrement, \
        col_fname text, \
        col_lname text, \
        col_email text \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("insert into tbl_persons(col_fname, col_lname, \
        col_email) values (?,?,?)", \
        ('sara','jones','sjones@gmail.com'))
    cur.execute("insert into tbl_persons(col_fname, col_lname, \
        col_email) values (?,?,?)", \
        ('dale','white','honkeytonk@gmail.com'))
    cur.execute("insert into tbl_persons(col_fname, col_lname, \
        col_email) values (?,?,?)", \
        ('god','zilla','rrraaarrrrrhhh@gmail.com'))
    cur.execute("insert into tbl_persons(col_fname, col_lname, \
        col_email) values (?,?,?)", \
        ('benicio','deltoro','bdtor@gmail.com'))
    conn.commit()
conn.close()
    
conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute('select col_fname,col_lname,col_email from tbl_persons where \
        col_fname = "sara"')
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}\
        ".format(item[0],item[1],item[2])

    print(msg)






