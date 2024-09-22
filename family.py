class Family():

    def __init__(self,age,name,relation):
        self.age=age
        self.name=name 
        self.relation=relation
    
    def show_details(self):
        print("The details of the family are:")
        print(self.age, self.name, self.relation)
    
    def change_details(self):
        self.age=input("Please enter the age here ")
        self.name=input("Please enter the name here ")
        self.relation=input("Please enter the relation here ")
    

father=Family("45","Saravanan","father")
mother=Family("43","Shanmugapriya","mother")
sister=Family("9","Nireekshana","sister")
brother=Family("0","none","none")

father.show_details()
mother.show_details()
sister.show_details()
brother.show_details()

father.change_details()
mother.change_details()
sister.change_details()
brother.change_details()

father.show_details()
mother.show_details()
sister.show_details()
brother.show_details()


