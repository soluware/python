import datetime
import random
h1 = datetime.datetime.utcnow()
resp = 0
for x in range(1, 11):
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    op = random.choice(["+", "-", "/", "*"])
    c = eval(str(a) + op + str(b))
    d = input(str(c))
    if c == int(d):
        resp += 1
print(str(resp)+"/"+str(x))
h2 = datetime.datetime.utcnow()
print(h2-h1)
