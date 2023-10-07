class Base:
# TODO: there's code missing in one or more lines below
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size

class Circle(Base):
    Shape = "circle"
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        '''self.x = x
        self.y = y
        self.size = size'''
        
    def shape(self):
        return f"This is a {self.Shape}"
        
    def draw(self):
        return f"""({self.x}, {self.y})
{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """

def main():
    c = Circle(1,2,3)
    print(c.shape())
    print(c.draw())

    
main()
