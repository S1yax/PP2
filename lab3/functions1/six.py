from itertools import permutations
def permutation(s):
    words = s.split()
    perms = permutations(words)
    for i in perms:
        print(" ".join(i)) 

a = input("Enter the sentance: ")
permutation(a)