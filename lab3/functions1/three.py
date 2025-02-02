def solve(numheads, numlegs):
    print(2*numheads-(numlegs)/2,"chicken")
    print((numlegs)/2-numheads,"rabbits")
numheads=int(input("Enter numheads count "))
numlegs=int(input("Enter numlegs count "))
print(solve(numheads, numlegs))

