#!"C:\Users\student\AppData\Local\Programs\Python\Python37-32\pythonw.exe"
print("Content-Type: text/html")
print()
import cgi
c=cgi.FieldStorage()
z=c.getvalue("create")
def accno():
    a=8
    f=''
    x=[x for x in range(a)]
    for y in range(a):
        import random as r
        f=f+str(r.choice(x))
        f=str(f)
    return(f)
def password():
    a=[chr(x) for x in range(ord('a'),ord('z')+1)]
    b=[chr(x) for x in range(ord('A'),ord('Z')+1)]
    c=10
    e=["#","%","@","&","*"]
    d=''
    x=[x for x in range(c)]
    for y in range(2):
        import random as r
        d=d+str(r.choice(a))
        d=d+str(r.choice(b))
        d=d+str(r.choice(x))
        d=d+str(r.choice(e))
        d=str(d)
    return(d)
def mail():
    import sqlite3
    a=sqlite3.connect("hey.db")
    a.execute('create table if not exists details(id integer primary key AUTOINCREMENT,username varchar(50),accno int,password varchar(50))')
    import urllib.request
    import smtplib
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('xxxx@gmail.com','12345')
    o=accno()
    k=password()
    SUBJECT='Account Number '+o
    TEXT='Password '+k
    message='subject: {}\n\n{}'.format(SUBJECT,TEXT)
    server.sendmail('xxxx@gmail.com','yyyy@gmail.com',message)
    print('thank you ur mail has been sent')
    a.execute('insert into details(username,accno,password)values(?,?,?)',("navin",o,k))
    a.commit()
    b=a.execute('select * from details')
    for c in b:
        print(c)
z=mail()



