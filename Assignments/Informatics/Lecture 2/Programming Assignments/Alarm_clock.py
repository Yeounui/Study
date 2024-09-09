'''
Created on 2016. 9. 13.

@author: korea
'''
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

if abs(h2-h1)<=12 :
    dh = abs(h2-h1)
else:
    if h1 < h2 :
        dh = abs(h2-(h1+24))
    else:
        dh = abs((h2+24)-h1)

if abs(m2-m1)<=30 :
    dm = abs(m2-m1)
else:
    if m1 < m2 :
        dm = abs(m2-(m1+60))
    else:
        dm = abs((m2+60)-m1)

print(dh+dm)