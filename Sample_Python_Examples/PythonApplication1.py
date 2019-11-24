import ast

lists=ast.literal_eval(input())
num_to_chk=int(input())

series2=[]

for i in lists:
    series2.append(int(i))

a=series2[0]
d=series2[1]-series2[0]

def ismember(current_value, difference, num_to_chk) :
    if (current_value == num_to_chk) :
        return True
    elif (current_value > num_to_chk) :
        return False
    else :
        return ismember(current_value+difference, difference, num_to_chk)

def ismember_v2(current_value, difference, num_to_chk) :
    if (current_value == num_to_chk) :
        return True
    elif (current_value < num_to_chk) :
        return False
    else :
        return ismember_v2(current_value-difference, difference, num_to_chk)

if ismember(a, d, num_to_chk) or ismember_v2(a, d, num_to_chk) :
    print(True)
else:
    print(False)
