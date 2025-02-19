import re
def reg():
    user_input = input("")
    matches = re.findall(r"[A-Z][a-z]+", user_input)
    print(matches)
reg()
