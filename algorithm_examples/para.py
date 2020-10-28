def para(string):
    openlist = ['(','[','{']
    closedlist = [')',']','}']
    checklist = []

    for i in string:
        if i in openlist:
            checklist.append(i)
        elif i in closedlist:
            position = closedlist.index(i)
            if ((len(checklist) > 0) and
                (openlist[position] == checklist[len(checklist)-1])):
                checklist.pop()
            else:
                return "Unbalanced"
    if len(checklist) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

string = "{[]{()}}"
print(string,"-", para(string)) 
  
string = "[{}{})(]"
print(string,"-", para(string)) 
  
string = "((()"
print(string,"-",para(string)) 