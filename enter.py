#!"C:\Program Files\Python36-32\pythonw.exe"
print("Content-Type: text/html")
print()
import cgi
import sqlite3
c=cgi.FieldStorage()
y=c.getvalue("name")
x=c.getvalue("passw")
a=sqlite3.connect("hey.db")
c=0
b=a.execute("select * from details where username=? and password=?",(y,x))
for c in b:
    pass
if c:
    print("login success")
    print("""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Page Title</title>
    </head>
    <body>
    <h1>Enter THE URL</h1>
    <form action="web.py">
    <input type="text" name="url">
    <input type="submit">
    </body>
    </html>
    """)
else:       
    print("login unsuccessful")

