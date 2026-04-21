class Car:
    def __init__(self, name, model, color, price):    # initializing the attributes
        self.name = name
        self.model = model
        self.color = color
        self.price = price
        
    def drive(self):
        print(f"I saw that You drive the {self.color} {self.name} in the narrow road of los amigos")     # init method to be used in normal method
        print(f"your car price is {self.price} and your model is {self.model}")
        
    def stop(self):
        print(f"You stop the {self.color},{self.name}") 
    