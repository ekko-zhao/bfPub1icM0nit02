
a=set()


for i in open('mortyread','r').readlines():
    a.add(i.replace('\n',''))

for j in a:
    print j