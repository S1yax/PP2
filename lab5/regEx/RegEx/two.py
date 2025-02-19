import re
def reg():
    user_input = input("")
    matches = re.findall(r"ab{2,3}", user_input)
    print(matches)
reg()
