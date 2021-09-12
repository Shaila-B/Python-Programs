import random
ran = random.Random()

def sum1():
    xs=[]
    for i in range(10000000):
        num=ran.randrange(1000)
        xs.append(num)
    tot = sum(xs)
    return tot
def sum2():
    tot=0
    for i in range(10000000):
        num=ran.randrange(1000)
        tot+=num
    return tot
print(sum1())
print(sum2())
