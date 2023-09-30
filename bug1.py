class Base:
# TODO: there's code missing in one or more lines below
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
    
class Circle(Base):
    def __init__(self, x, size):
        y = x
        super().__init__(x, y, size)
        '''self.x = x
        self.y = y
        self.size = size'''
        
    def shape(self):
        print("This is a circle")
        
    def draw(self):
        print(f"""({self.x}, {self.y}) 
{self.size}
            , - ~ ~ ~ - ,
        , '               ' ,
      ,                      ,
     ,                        ,
    ,                          ,
    ,                          ,
    ,                          ,
     ,                        ,
      ,                      ,
        ,                 , '
          ' - , _ _ _ , '
                 """)
def main():
    s = Circle(2,1)
    s.shape()
    s.draw()
    
main()
