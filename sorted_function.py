students = [
    ['Ali', [17, 18, 17,20]],
    ['Mina', [0, 0, 0,0]],
    ['Reza', [20, 0, 20, 20]],
    ['Sara', [9, 11, 7, 12]],
    ['Ahmad', [19, 16, 17, 19]]
    ]
#def avg(x):
#   return sum(x[1])/len(x[1])
#for i in sorted(students, key=avg, reverse=True):
#    print (avg(i), i)
 
for i in sorted (students, key=lambda x:  sum(x[1])/len(x[1]), reverse=True):
    print(i)
    
