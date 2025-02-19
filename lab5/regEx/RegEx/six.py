import re
def reg():
    user_input = input("")
    matches = re.sub(r"[ ,\.]", ":", user_input)
    print(matches)
reg()
