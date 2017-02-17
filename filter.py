import re
a,b = raw_input("").split(' ')
g=open(b,'r+')
with open (a) as f:
    for line in f:
        for x in re.findall('[A-Za-z0-9\.\_\%\+\-]+@[A-Za-z0-9\.\-]+\.[A-Za-z]{2,3}\.*[A-Za-z]*',line):
            g.write(x+"\n")
g.close()
f.close()
