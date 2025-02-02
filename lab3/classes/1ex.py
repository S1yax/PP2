
class String:
    def __init__(self, string):
        self.string = string

    def print_str(self):
        print(self.string)

print("Type a text you want:")
x = String(str(input()))
x.print_str()

class answer:
    def __init__(self):
        self.userstr = ''
    def getstring(self):
        self.userstr = str(input())
    def printstring(self):
        self.userstr = print(self.userstr.upper())
        self.userstr
ans = answer()
ans.getstring()
ans.printstring()