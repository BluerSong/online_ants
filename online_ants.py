import time
import requests
from requests_html import HTMLSession
import base64
d = 1
e = 1
j = input("保存路径>>>")
while d < 2:
    g = str(e)+".txt"
    f = 0
    c = str(input("输入网址>>>"))
    session = HTMLSession()
    r =session.get(c)
    file = open(str(j)+"\\"+str(g),'w',encoding = 'utf-8')
    a = r.html.text
    file.write(a)
    file.close()
    while f < 1:
        try:
            d = int(input("是否继续,1 是 2 否"))
        except:
            f += 0
        else:
            f += 1
            e += 1




