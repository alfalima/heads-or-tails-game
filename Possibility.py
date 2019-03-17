import random

random_list = []
total_list = []

def randomNunber():
    x  = random.randint(0, 1)
    random_list.append(x)

    if x == 0:
        randomNunber()

i = 0
while i < 900000:
    randomNunber()
    print(random_list)
    benefit = 2**len(random_list)
    total = benefit - 100  # 100$ for Incoming fee
    total_list.append(total)
    print(total)
    random_list.clear()
    i = i + 1


total_list.sort()
print(total_list)
sum_total_list= total_list
b =sum(i for i in sum_total_list)
print(b)
