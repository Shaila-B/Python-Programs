class animal:
    def display(self):
        print('Bow Bow!!')
class dog(animal):
    def display(self):
        print('Bow Bow!!')
class cat(dog):
    def display(self):
        print('Mew mew!')

obj=cat()
obj.display()

    
