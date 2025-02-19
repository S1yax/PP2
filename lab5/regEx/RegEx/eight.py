import re
def reg():
    user_input = input()
    parts = re.split(r'(?=[A-Z])', user_input)
    print(parts)
reg()
