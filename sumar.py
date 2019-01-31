import datetime
import random
h1 = datetime.datetime.utcnow()
resp = 0
for x in range(1, 11):
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = a + b
    d = input(str(a)+" + "+str(b)+" = ")
    if c == int(d):
        resp += 1
print(str(resp)+"/"+str(x))
h2 = datetime.datetime.utcnow()
print(h2-h1)
