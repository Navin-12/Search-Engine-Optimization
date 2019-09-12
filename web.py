#!"C:\Program Files\Python36-32\pythonw.exe"
print("Content-Type: text/html")
print()
def web():
    import cgi
    import xlsxwriter as x
    import os
    c=cgi.FieldStorage()
    z=c.getvalue("url")
    import urllib.request
    z='http://'+z
    b=urllib.request.urlopen(z)
    import bs4
    b=bs4.BeautifulSoup(b,'html.parser')
    for c in b(['script','style']):
        c.extract()
    e=b.get_text()
    f=e.split(' ')
    h=open('get.txt','r')
    h=h.read().split(" ")
    g={}
    for z in f:
        if z not in h:
            i=f.count(z)
            g[z]=i
    #print(g)
    sor=sorted(g.items(),key=lambda t:t[1],reverse=True)
    tu=sor[0:5]
    print(tu)
    p=x.Workbook('let.xlsx')
    q=p.add_worksheet("hari")
    q.write(0,0,'keys')
    q.write(0,1,'values')
    row=1
    col=0
    for z in range(5):
        q.write(row,col,tu[z][0])
        q.write(row,col+1,tu[z][1])
        row+=1
    p.close()
    os.system("let.xlsx")
web()
