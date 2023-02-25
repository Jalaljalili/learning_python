##Example 1

name = ['ali', 'sara' , 'Reza']
new_name = [x.upper() for x in name]
print (new_name)


##Example 2

number = [10,11,12,13,14,15]
new_number = [x**2 for x in number if x %2 !=0]
print (new_number)

## Example 3

n1 = [0, 4, 2]
n2 = [3, 5, 8]

result1 = []
for x in n1:
    for y in n2:
        if n1.index(x) == n2.index(y):
            result1.append(x*y)
print (result1)
###with list comprehension

result2 = [x*y for x in n1 for y in n2 if n1.index(x) == n2.index(y)]
print (result2)

#### OR
for i in  [x*y for x in n1 for y in n2 if n1.index(x) == n2.index(y)]:
    print (i)
