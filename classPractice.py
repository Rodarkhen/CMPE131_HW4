class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"
    
Corolla = Car('silver', 140000)
Civic = Car('blue', 12000)
print(Corolla)
print(Civic)