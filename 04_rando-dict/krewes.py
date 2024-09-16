'''
Sasha Murokh
No Zs
SoftDev
K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
2024-9-16
time spent: 0.25
'''

import random
krewes = {3:['Jonathan','Alex','Naf'], 42:['Jonathan','Alex','Naf'], 888:['Jonathan','Alex','Naf']}

def randoselect():
    x=int(random.random()*3)
    lis=list(krewes.keys())
    z=int(random.random()*3)
    print((krewes.get(lis[x]))[z])

randoselect()