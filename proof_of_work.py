from hashlib import sha256
from time import time
from random import randint

x= randint(0,10000)
y=0
t1 = time()
while (sha256(f'{x*y}'.encode()).hexdigest()[:6] != '123456'):
    print(y)
    y +=1

print("x = {}".format(x))
print("y = {}".format(y))
print(sha256(f'{x*y}'.encode()).hexdigest())
t2= time()
print(t2-t1)

# x = 5385
# y = 21069182
# hash(x*y) = 123456432081821574050d2ee4a7acef0f94a52a1011a77ad5e2f37543cf8629
# total_time_to_find_y = 92.40833306312561