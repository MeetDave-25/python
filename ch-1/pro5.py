list_1 = ["apple","banana","kiwi"]
list_2 = ["banana","orange","chickoo"]

#lists to store result
com_list = []
non_list = []

#Find common elements
for item in list_1:
    if item in list_2:
        com_list.append(item)

#find non-common elements from list_1
for item in list_1:
    if item not in list_2 :
        non_list.append(item)

#find non-common elements from list_1
for item in list_2:
    if item not in list_1 :
        non_list.append(item)    

#display
print("common element : ",com_list)
print("non common elements :- ",non_list) 
