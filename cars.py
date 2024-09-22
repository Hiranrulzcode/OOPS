class Cars():

    def __init__(self, brand, color, speed_limit, mileage):
        self.color=color
        self.brand=brand
        self.speed_limit=speed_limit
        self.mileage=mileage
    
    def car_start(self):
        print("Car started")
    
    def car_stop(self):
        print("Car stopped")
    
    def car_accelerating(self):
        print("Car has accelerated")
    
    def show_details(self):
        print("The details of the car are:")
        print(self.brand, self.color, self.speed_limit, self.mileage)
    
    def change_details(self):
        self.brand=input("Please enter brand")
        self.color=input("Please enter color")
        self.speed_limit=input("Please enter speed_limit")
        self.mileage=input("Please enter mileage")
    

Audi_Q3=Cars("Audi", "Grey","240 kph", "100 km combined")
Audi_Q3.car_start()
Audi_Q3.car_accelerating() 
Audi_Q3.car_stop()
Audi_Q3.show_details()
Audi_Q3.change_details()
Audi_Q3.show_details()




