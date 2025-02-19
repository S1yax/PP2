import re

def reg():
    user_input = input()
    new = re.sub(r'[_]+', ' ', user_input)
    spl = new.split()
    if not spl:
        print("")
        return
    new_verb = spl[0].lower() + ''.join(word.capitalize() for word in spl[1:])
    print(new_verb)

reg()
