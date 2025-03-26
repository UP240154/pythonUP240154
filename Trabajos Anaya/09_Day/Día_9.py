##Nivel 1

## 
age=int(input("Enter your age"))
if age >= 18:
        print("You are old enough to drive")
else:
        print(18-age)

##
my_age=19
your_age=int(input("Enter your age"))
if my_age>your_age:
    dif1=my_age-your_age
    if dif1==1:
        print("You are 1 year younger than me")
    else:
        print("You are ",dif1," years younger than me")
else:
    dif2=your_age-my_age
    if dif2==1:
        print("You are 1 year older than me")
    else:
        print("You are ",dif2," years older than me")
##
a=int(input("Enter a number"))
b=int(input("Enter a number"))
if a>b and a==b:
    if a==b:
         print("both are equal")
    else:
         print(a, "is greater than", b)
else:
    print(b, "is greater than", a)

##Level 2
cal = {
    'A': range(80, 101),
    'B': range(70, 80),
    'C': range(60, 70),
    'D': range(50, 60),
    'F': range(0, 50)
}

cali = int(input('Cuál es tu calificación?'))
grade = None
for key, val in cal.items():
    if cali in val:
        grade = key
        break

print(grade)

