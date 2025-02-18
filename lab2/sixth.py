thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict.get("model")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

thosdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thosdict["year"] = 2018
thosdict.update({"brand": "toyota"}) 
print(thosdict)

