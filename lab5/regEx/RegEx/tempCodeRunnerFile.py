import re
def reg():
    user_input = input("")
    patt = r'[_]+'
    new = re.sub(patt , ' ' , user_input)
    spl = list(new.split())
    new_verb = ''
    for i in spl:
        verb = i.capitalize()
        new_verb += verb
reg()
