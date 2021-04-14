# list comprehensions
par = [i for i in range(1, 100) if i % 2 == 0]
imp = [j for j in range(1, 100) if j % 2 != 0]

print(par)
print(imp)
print('*'*95)

# generators
par1 = [i for i in range(100) if i % 2 == 0]

#print(par1.next())

# sum of all num par
sum_par = sum(j for j in range(1, 100) if j % 2 == 0)
print(sum_par)

