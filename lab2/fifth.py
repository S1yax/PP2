thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

thisset.remove("banana")
print(thisset)

for x in thisset:
  print(x)

print("banana" not in thisset)

print("banana" in thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print(thisset)

