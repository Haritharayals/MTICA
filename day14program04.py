class Wolf:
    price=500
    def __init__(self,name,color):
        self.color=color
        self.name=name
    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark1(self):
        print("woof")
        

    
if __name__=="__main__":
    pet1=Dog("Tommy","brown")
    pet1.bark()
    pet1.bark()
    
    print(pet1.name,'is of color',pet1.color)
    

   
