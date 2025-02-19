import re
def reg():
    user_input = input("")
    matches = re.findall(r"[a-z]+_[a-z]+", user_input)
    print(matches)
reg()
