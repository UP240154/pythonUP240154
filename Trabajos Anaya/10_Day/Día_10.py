##
count=0
while count<11:
    print(count)
    count=count + 1

numbers=[1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    print(i)

##
while -1<count:
    print(count)
    count=count - 1

inum=[10,9,8,7,6,5,4,3,2,1]
for i in inum:
    print(i)

##
gato=0
while gato<8:
    print('#'*int(gato))
    gato=gato + 1

##
fila=0
columna=8

for i in range(fila):
    for j in range(columna):
        print('#', end='')
    print()

##
num=0

while num<11:
    print(num, 'x', num, '=', num*num)
    num=num + 1

##
nom=['Python', 'Numpy','Pandas','Django', 'Flask'] 
for i in nom:
    print(i)

##
for i in range(101):
    if i%2==0:
        print(i)

for i in range(101):
    if i%2!=0:
        print(i)

i=0

##Level 2

for i in range(101):
    for j in range(100):
        i=i+j

print(i)

##
for i in range(101):
    for j in range(100):
        if i%2==0 and j%2==0:
            i=i+j
print(i)

sum=0
for i in range(101):
    if i%2!=0:
        sum=sum+i
print(sum)

##Level 3

##
from lista_paises import countries

paisesland=[countries for countries in countries if 'land' in countries]
print(paisesland)

##
fruits = ['banana', 'orange', 'mango', 'lemon']
conteo=-1
for i in fruits:
    print(fruits[conteo])
    conteo=conteo -1




