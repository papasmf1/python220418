class GString:
    def __init__(self, init=None):
        self.content = init 
        
    def __sub__(self, str):
        for i in str:
            self.content = self.content.replace(i, '')
        return GString(self.content)
    
    def __abs__(self):
        return GString(self.content.upper())
    
    def print(self):
        print(self.content); 
    
g = GString("aBcdef")
g -= "df"
g.print()
g = abs(g)
g.print() 

    
