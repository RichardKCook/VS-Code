
#working with many args
def add(*args):
    print(sum(args))

add(1,2,3,4,5,6,7)



def calculate(n, **kwargs):

    for key,value in kwargs.items():
        print(key)
        print(value)
    n+=kwargs["add"]
    n*=kwargs["mult"]
    print(n)

    print(kwargs["add"])


calculate(2, add=3, mult=5)    


#Use .get() to get values from dictionary
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GTR")

print(my_car.model, my_car.make)