n = int(input())
def even(a):
    for i in range(a+1):
        if i % 2 == 0 and i != 0:
            yield i
sq = even(n)
arr = list(sq)
new_arr=str(arr)
answer = ",".join(new_arr)
print(new_arr)