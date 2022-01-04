num = int(input('Digite um número que te mostro a tabuada dele: '))
print(10*'-')
for i in range(11):
    print('{} * {:2} = {}'.format(num, i, num*i))
print(10*'-')
