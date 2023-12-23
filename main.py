class cat:
    def __init__(self, name):
        self.name=name
        self.gladness=50
        self.famine=50
        self.alive=True

    def to_eat(self):
        print("time to eat")
        self.progress+=1
        self.famine-=5
    def to_sleep(self):
        print("I will sleep")
        self.progress+=3
    def to_chill(self):
        print("Rest time")
        self.gladness+=5
        self.famine+=2.5
    def is_alive(self):
        if self.famine<+75:
            print("The cat died of hungrer..")
            self.alive=False
        elif self.gladness<=0:
            print("Depresion..")
            self.alive=False
        elif self.famine<:100
            print("The cat ate too much")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"famine - {round(self.famine,2)}")

    def live(self,day):
        day="Day" + str(day) + "of" = self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.to_eat()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()
Murka=cat(name="Murka")
for day in range(365):
    if Murka.alive==False
        break
    Murka.live(day)