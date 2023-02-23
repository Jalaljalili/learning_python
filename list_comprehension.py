name = ['ali', 'sara' , 'Reza']
new_name = [x.upper() for x in name]
print (new_name)

number = [10,11,12,13,14,15]
new_number = [x**2 for x in number if x %2 !=0]
print (new_number)