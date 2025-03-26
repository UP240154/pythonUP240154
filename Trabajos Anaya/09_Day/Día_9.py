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
##
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

##
season = {
    'winter': 'December, January, February',
    'spring': 'March, April, May',
    'summer': 'June, July, August',
    'autumn': 'September, October, November'
}

month = input('Enter the month: ')
for key, val in season.items():
    if month in val:
        print(key)
        break

##
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=input("Enter a fruit")
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(fruits)

##
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
}}
if 'skills' in person:
    if 'skills' in person:
        skills = person['skills']
        middle_index = len(skills) // 2
        print(skills[middle_index])
    if 'Python' in skills:
        print("Python is in the skills")
    else:
        print("Python is not in the skills")

if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print('He is a front end developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
else:
        print('unknown title')

if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")