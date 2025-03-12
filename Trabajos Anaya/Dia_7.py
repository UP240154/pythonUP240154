##Nivel 1

##
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

##
it_companies.add('Twitter')
print(it_companies)

##
it_companies.update(['Samsung', 'IBM'])
print(it_companies)

##
it_companies.remove('IBM')
print(it_companies)

##
it_companies.discard('Huawei')
print(it_companies)

##Level 2

##
print(A.union(B))

##
print(A.intersection(B))

##
print(A.issubset(B))

##
print(A.isdisjoint(B))

##
print(A.union(B))
print(B.union(A))

##
print(A.symmetric_difference(B))

##
del A
del B

##Level 3
age_st=set(age)
print(len(age_st))
print(len(age))

nombre="Alberto"    #string
lista=[1,2,3,4,5]   #list
tupla=(1,2,3,4,5)   #tuple
set1={1,2,3,4,5}    #set

oracion='I am a teacher and I love to inspire and teach people'.split()
l1=[]
count=0

for item in oracion:
    if item not in l1:
        count+=1
        l1.append(item)

print(count)