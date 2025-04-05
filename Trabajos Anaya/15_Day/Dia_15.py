##SyntaxError
##print('hello world; No se ha cerrado la comilla
print('hello world')

##NameError
##print(age); No se ha definido la variable age
age = 25
print(age)

##IndexError
##numbers = [1, 2, 3, 4, 5]
##print(numbers[5]); El indice 5 no existe en la lista
numbers = [1, 2, 3, 4, 5]
print(numbers[4])

##ModuleNotFoundError
##import math1; No existe la libreria math1
import math
print(math.sqrt(16))

##AtributeError
##math.pi; No se puede acceder a pi sin importar la libreria math
import math
print(math.pi)

##KeyError
##users = {'name':'Asab', 'age':250, 'country':'Finland'}
#print(users['nme']); No existe la clave 'nme' en el diccionario
users = {'name':'Asab', 'age':250, 'country':'Finland'}
print(users['name'])
print(users['country'])


## TypeError
##4+'3'; No se puede sumar un string con un entero
print(4 + float('3'))

##ImportError
## from math import power; no se puede importar una funcion de la libreria math con el nombre power
from math import pow
print(pow(2,3))

## ValueError
##int('12a'); No puede haber un string con letras
print("           ")
print(int('12'))

##ZeroDivisionError
#print(1/0); No se puede dividir entre 0
print(1/2)
