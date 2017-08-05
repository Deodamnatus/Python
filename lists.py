shopping_list = ["Eggs", "Milk", "Flour"]

print(shopping_list[0])
#ouputs Eggs

shopping_list[2]= "Peas"
#replaces Milk with Peas

shopping_list.append("Carrots")
#adds item to list

if "Peas" in shopping_list and "Carrots" in shopping_list:
    print("Don't forget the peas and carrots!!!")
print("Double check that you have all {0} items!!!".format(len(shopping_list)))
#prints list out

del shopping_list[1]
print("They already got milk at the store earlier and forgot to take it off the list there we go!")

for item in shopping_list:
    print(item.lower())