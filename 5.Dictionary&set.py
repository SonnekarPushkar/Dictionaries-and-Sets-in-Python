#                                          ||DICTIONARY||
'''
mydict= {
    "Name" :"Pushkar",
    "School":"Narayana",
    "Language":"Python",
    "Marks":[1,2,3,23.6],
    "anotherdict":{'Harry':'Potter'}

}
'''
'''
print(mydict['Name'])
print(mydict['School'])
print(mydict['Language'])
print(mydict['anotherdict']['Harry'])
mydict['Marks']=[23,45]
print(mydict)
'''

#Dictionary methods:

#1.keys() #prints keys of the dictionaries
'''
print(mydict.keys())
'''

#2.values() #prints the values
'''
print(mydict.values())
'''

#3.items() #prints the ('key','value') for all content
'''print(mydict.items())'''

#4.update() #adds something more to existinf=g dictionary
'''
updateDict = {
    "Friend":"Utkarsh"
}
mydict.update(updateDict)
print(mydict)
'''
#5.get() #gives value for entered key
'''print(mydict.get('Name'))'''

#More methods on docs.python.org

#                                                ||SETS||

#sets do not consider repetative elements
'''
a = {1,2,3,4,1}
print(a) 
print(type(a))
'''
#An empty set can be created using the below syntax
'''
a = set()
print(type(a))
'''
#Methods in sets:
b={4,5}
#1.add() #anything added to the list which is repatative would not be considered
'''
b.add(5)
print(b)
''' #lists cannot be added in sets but tuples can be added . Dictionaries can't be added too
#2.len() prints the length of the set
'''print(len(b))'''

#                                        ||PRACTICE QUESTIONS||

#Question 1 :
'''
lan = {
    "Vastu":"Item",
    "Naam":"Name",
    "Saeb":"Apple"
}
a = input("Enter the hindi word :")
print("The english meaning for ",a," is ",lan[a])
'''

#Question 3 :
'''
mydict = {
    "Number1":"18",
    "Number2":18
}
print(mydict)

#Yes , we can definately have 18 as int and str in value place in a set
'''