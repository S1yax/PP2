s = input()
s = s.lower()
t = ''.join(reversed(s))
if t == s:
    print('True')
else:
    print('False')
