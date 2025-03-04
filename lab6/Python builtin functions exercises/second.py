s=str(input())
uppe=0
lowe=0
for char in s:
    if char.isupper():
        uppe+=1
    elif char.islower():
        lowe=+1
print("There are ",uppe," upper case letters and ",lowe,"lower case letters")
