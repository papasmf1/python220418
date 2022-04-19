str = "Not Class Member"
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(str)

g = GString()
g.set("First Message")
g.print()
