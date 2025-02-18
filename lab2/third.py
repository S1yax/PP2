nlist = ["apple", "banana", "cherry"]
print(nlist)
print(len(nlist))


mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

klist = ["apple", "banana", "cherry"]
klist.insert(2, "watermelon")
print(klist)

alist = ["apple", "banana", "cherry"]
alist.insert(1, "orange ")    #append or insert
print(alist)

thoslist = ["apple", "banana", "cherry"]
for x in thoslist:
  print(x)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

