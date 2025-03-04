##Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
T="thirty_"
D="days_"
F="of_"
P="python_"
TDFP=(T+D+F+P)
print(TDFP)

##Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
C="Coding_"
fo="For_"
A="All_"
CfoA= C+fo+A
print (CfoA)

##Declare a variable named company and assign it to an initial value "Coding For All".
company=CfoA
print(company)

##Print the length of the company string using len() method and print().
print(len(company))

##Change all the characters to uppercase letters using upper() method.
print(company.swapcase())

##Change all the characters to lowercase letters using lower() method.
print(company.swapcase().swapcase())

##Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.swapcase().swapcase().capitalize())

##Cut(slice) out the first word of Coding For All string.
language = company.swapcase().swapcase().capitalize()
Coding=language[0:6]
print(Coding)

##Check if Coding For All string contains a word Coding using the method index, find or other methods.
index=language
if "Coding" in language:
    print("Coding is in Coding for all")

##Replace the word coding in the string 'Coding For All' to Python.
print(language.replace("Coding", "Python"))

##Change Python for Everyone to Python for All using the replace method or other methods.
print(language.replace("Coding", "Python").replace("all", "everyone"))

##Split the string 'Coding For All' using space as the separator (split()) .
print(language.split())

##"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
marca="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(marca.split(', '))

##What is the character at index 0 in the string Coding For All.
print(language[0:1])

##What is the last index of the string Coding For All.
print(language[13:14])

##What character is at index 10 in "Coding For All" string.
print(language[9:10])

##
print((language.split('_'))[0:1])