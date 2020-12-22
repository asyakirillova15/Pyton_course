from itertools import count
from itertools import cycle

for i in count(3, 1):
    if i > 7:
        break
    else:
        print(i)

c = 0
for n in cycle(['ура!', 'скоро', 'Новый год']):
    if c > 8:
        break
    else:
        print(n)
        c += 1

my_cycle = cycle([12, 23, 123, 'hi'])
my_flag = True
while my_flag:
    for i in count(3, 1):
        if i > 10:
            my_flag = False
        else:
            print(i, next(my_cycle))
