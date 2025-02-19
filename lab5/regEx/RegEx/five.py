import re
def reg():
    user_input = input("")
    matches = re.findall(r"[a][b]+", user_input)
    print(matches)
reg()
