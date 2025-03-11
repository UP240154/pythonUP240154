##
tp=()

##
tpls=('Kimby', 'Claudia')
tplb=('Gerardo', 'Manuel')

##
tpl=(tpls+tplb)
print(tpl)

##
print(len(tpl))

##
family_members=tpl+('Alberto', 'Corina')
print(family_members)

##Level 2

##
padres=(family_members[4:6])
print(padres)
print(tpl)

##
fruta=('manzana', 'pera', 'uva', 'sandia', 'melon', 'platano')
verdura=('tomate', 'cebolla', 'lechuga', 'pepino')
carne=('huevo', 'pollo', 'pescado', 'res')
food_stuff_tp=(fruta+verdura+carne)
print(food_stuff_tp)

##
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)

##
print(food_stuff_lt[int(len(food_stuff_lt)/2)])

##
print(food_stuff_lt[0:2])
print(food_stuff_lt[11:14])

##
del food_stuff_tp

##
'manzana' in tp

##
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

'Estonia' in nordic_countries
'Iceland' in nordic_countries

