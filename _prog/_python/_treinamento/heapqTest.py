import heapq

a = 1
nums = list()

while a <= 5:
    num = int(input('Informe %dº num: '%a))
    nums.append(num)
    a += 1

print('Maior num: %s'%(heapq.nlargest(1, nums)))
print('Menor num: %s'%(heapq.nsmallest(1, nums)))

