ht = int(input('Horas trabalhadas ao mês -> '))
vt = float(input('Valor por horas trabalhadas -> '))
pd = int(input('Percentual de desconto -> '))

sb = ht * vt
td = (pd / 100) * sb
sl = sb - td
print('******************************************************')
print('Horas Trabalhadas.................: {} horas'.format(ht))
print('Salário Bruto.....................: {:.2f} Ndbs'.format(sb))
print('Total Desconto....................: {:.2f} Ndbs'.format(td))
print('Salário Líquido...................: {:.2f} Ndbs'.format(sl))
print('******************************************************')
