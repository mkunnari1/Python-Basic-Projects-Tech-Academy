
import sqlite3, os

def conn():
    
    dbconn = sqlite3.connect('drill103.db')
                         
    with dbconn:
       cur = dbconn.cursor()
       cur.execute('create table if not exists tbl_files(\
            ID integer primary key autoincrement, \
            col_FileName string)')
    
       dbconn.commit()
    dbconn.close()

conn()
                             
def returnFiles():

    import os
    listDir= os.listdir("C:\\Users\\HP\\OneDrive\\Documents\\Python-Projects\\Python-Basic-Projects-Tech-Academy\\drillFilesPage103\\")
    
    fPath = 'C:\\Users\\HP\\OneDrive\\Documents\\Python-Projects\\Python-Basic-Projects-Tech-Academy\\drillFilesPage103\\'

    for file in listDir:
        if file.endswith('.txt'):
            return(file)



     

def getFiles():

    import os, sqlite3
    listDir= os.listdir("C:\\Users\\HP\\OneDrive\\Documents\\Python-Projects\\Python-Basic-Projects-Tech-Academy\\drillFilesPage103\\")
    
    fPath = 'C:\\Users\\HP\\OneDrive\\Documents\\Python-Projects\\Python-Basic-Projects-Tech-Academy\\drillFilesPage103\\'

    for file in listDir:
        if file.endswith('.txt'):
            print(file+' has been added to the database')
            
            dbconn = sqlite3.connect('drill103.db')

            with dbconn:
                cur= dbconn.cursor()
                cur.execute("insert into tbl_files(col_FileName) values(?)", (file,))
                dbconn.commit()
            dbconn.close()

dbData = getFiles()



'''def addDb():
            
    dbconn = sqlite3.connect('drill103.db')

    with dbconn:
        cur = dbconn.cursor()
        cur.execute("insert into tbl_files(col_FileName) value(?)", \
                    (dbData))
        dbconn.commit()
    dbconn.close()

addDb()'''

