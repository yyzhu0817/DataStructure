"""
若n1+n2+n3=1000,且n1^2+n2^2=n3^2(n1,n2,n3为自然数),求出所有n1、n2、n3可能的组合
"""
import time
start = time.time()

for n1 in range(0, 1001):
    for n2 in range(0, 1001):
        n3 = 1000 - n1 - n2
        if n1 ** 2 + n2 ** 2 == n3 ** 2:
            print(n1, n2, n3)
stop = time.time()
print(f'耗时: {stop - start}')
