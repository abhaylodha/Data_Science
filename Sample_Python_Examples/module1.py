import ast

lists=ast.literal_eval(input())

list1=lists[0]
list2=lists[1]

i=0
j=0
list3=[]

while (i < (len(list1))  and j < (len(list2)) ) :
    if (list1[i] == list2[j]) :
        list3.append(list1[i])
        i = i + 1
        j = j + 1
    elif (list1[i] < list2[j]) :
        i = i + 1
    else :
        j = j + 1

print(list3)
