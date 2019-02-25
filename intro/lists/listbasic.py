#.append is used to add to the list
#.extend is used to add multiple values to the list
#.insert is used to add to a specific spot in list (position, type)
#.clear will remove all of the items in the list
#.pop will remove the index you pass in, or by default the last thing in the list
#.remove will remove the actual value you pass in
#.index will return the index of value in the list
#.count will return how many times the value occurs in the list
#.reverse will reverse the order of the list in place
#.sort will sort in ascending order
#.join will join strings together ' '.join(list3)
#slicing will slice a list and make another list from it some_list[start:end:step]



list1 = ["bananas", "apples", "towel"]
list2 = list(range(1,100))
list3 = []


print("Is 99 in the list?")
if 99 in list2:
	print("True\n")
print("Is 100 in the list?")
if 100 in list2:
	print("True\n")
else:
	print("False\n")

for i in list1:
	print(i)

print("")
i = 0
while i < len(list1):
	print(list1[i])
	i+=1

i = 0

while i < len(list1):
	print(f"{i}: {list1[i]}")
	i+=1

result = ''
for k in list1:
	result += k

result = result.upper()
print(result)

list3.append(400)
list3.extend([100, 200, 300])
print(list3)

list3.sort()
print(list3)

list3.insert(len(list3), "last")
print(list3)

list3.clear()
print(list3)

list3.extend([3,2,1])
print(list3)

list3.pop(0)
print(list3)

list3.pop()
print(list3)

list3.remove(2)
print(list3)

list3.extend(["Hello", "my", "name", "is", "Bailey"])
print(list3)
list3string = ' '.join(list3)
print(list3string + "!")

list4 = list3[1:4:1]
list4string = ' '.join(list4)
print(list4string + " bailey")
list5 = list3[:]
print(list5)

list5[0], list5[1] = list5[1], list5[0]
print(list5)
