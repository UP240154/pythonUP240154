##
def add_two_numbers(a,b):
    num=a + b
    return num
print (add_two_numbers(5,3))

##
def area_circle(r):
    area=3.14*r**2
    return area

print (area_circle(5))

##
def sum_total(*args):
    total=0
    for i in args:
        total=total + i
    return total
print (sum_total(1,2,3,4,5))

##
def temp(C):
    F=(C*9/5)+32
    return F
print (temp(30))

##
def check_season(mes):
    if mes in ['December', 'January', 'February']:
        return 'Winter'
    elif mes in ['March', 'April', 'May']:
        return 'Spring'
    elif mes in ['June', 'July', 'August']:
        return 'Summer'
    elif mes in ['September', 'October', 'November']:
        return 'Autumn'
print (check_season('January'))

##
def calculate_slope(x1,y1,x2,y2):
    slope=(y2-y1)/(x2-x1)
    return slope
print (calculate_slope(1,2,3,4))

##
def solve_quadratic_eqn(a,b,c):
    x1=(-b+((b**2)-4*a*c)**0.5)/(2*a)
    x2=(-b-((b**2)-4*a*c)**0.5)/(2*a)
    return x1,x2
print (solve_quadratic_eqn(1,2,3))

##
def print_list(lst):
    for i in lst:
        print(i)
print_list([1,2,3,4,5])

##
def reverse_list(lst):
    return lst[::-1]
print (reverse_list([1,2,3,4,5]))

##
def capitalize_list(lista):
    return [i.upper() for i in lista]
print (capitalize_list(['Potato', 'Tomato', 'Mango', 'Milk']))

##
def add_item(comida):
    food_staff=['Potato', 'Tomato', 'Mango', 'Milk']
    return (food_staff.append(add_item(comida)))

print(add_item('meat'))


