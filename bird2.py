class Bird():

    def __init__(self,color,species,size,legs):
        self.color=color
        self.species=species
        self.size=size
        self.legs=legs
    
    def bird_fly(self):
        print("Bird is flying")  
    
    def bird_stop(self):
        print("Bird stopped")
    
    def bird_tweet(self):
        print("Bird tweeted")
    
    def show_details(self):
        print("The features of this bird are: ")
        print(self.color, self.species, self.size, self.legs)
    
    def change_details(self):
        self.color=input("Please enter color ")
        self.species=input("Please enter species ")
        self.size=input("Please enter size ")
        self.legs=input("Please enter how many legs there are ")


Rufous=Bird("Blue", "Hummingbird","Small", "2 legs")
Rufous.bird_fly()
Rufous.bird_stop() 
Rufous.bird_tweet()
Rufous.show_details()
Rufous.change_details()
Rufous.show_details()


