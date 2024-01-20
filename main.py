import random
class Olena:
    def __init__(self, name="Olena", cat=None):
        self.name = name
        self.cat = cat
        self.gladness = 25
        self.progress = 50
        self.famine = 20
    def to_study(self):
        print("time to study")
        self.progress+=5
        self.gladness-=5
        self.famine+=2
    def to_sleep(self):
        print("I will sleep")
        self.gladness+=0.5
        self.famine+=2
        self.progress+=0
    def to_chill(self):
        print("Rest time")
        self.progress+=0.1
        self.gladness+=0.5
        self.famine+=2
    def to_TikTok(self):
        print("I need TikTok")
        self.progress-=0.5
        self.gladness+=1
        self.famine+=2
    def to_Music(self):
        print("I need listening to misic ")
        self.progress-=0.5
        self.gladness+=1
        self.famine+=2
    def to_Eat(self):
        print("I'm hangry ")
        self.progress-=0.5
        self.gladness+=1
        self.famine-=10
    def to_play_with_cat(self):
        print("I will play with Murka")
        self.progress -= 0.5
        self.gladness += 2
        self.famine -= 1
    def to_feed_the_cat(self):
        print("Murka want eat")
        self.progress -= 0.5
        self.gladness += 2
        self.famine -= 1
    def to_walk_with_cat(self):
        print("I'll walk with cat")
        self.progress -= 0.5
        self.gladness += 3
        self.famine -= 2
    def get_Cat(self):
        if self.cat is None:
            self.get_cat()
            print(f"I don't have a cat? I'm going to get cat {self.breed_of_cat}")
            breed_of_cat=random.randint(1, 4)
    def is_alive(self):
        if self.progress<-10:
            print("I'm stupid. Depresion. To hang")
            self.alive=False
        elif self.gladness>=0:
            print("you are nothing, you need to die)")
            self.alive=False
        elif self.progress>70:
            print("Yuhu ou passed externeli. But you couldn't build a normal independent life)")
            self.alive=False
        elif self.famine>75:
            print("You die)")
            self.alive=False
        elif self.famine<5:
            print("you ate too much and burst")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress,2)}")
        print(f"Famine - {round(self.famine,3)}")

    def live(self,day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,7)
        if live_cube==1:
            self.to_study()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        elif live_cube == 4:
            self.to_TikTok()
        elif live_cube == 5:
            self.to_Music()
        elif live_cube == 6:
            self.to_Eat()
        elif live_cube == 7:
            self.to_play_with_cat()
        elif live_cube == 8:
            self.to_feed_the_cat()
        elif live_cube == 9:
            self.to_walk_with_cat()
        self.end_of_day(),
        self.is_alive()
    breed_of_cat = {
        "Bombay cat": {"famine": 24, "joy": 75},
        "Bengal cat": {"famine": 20,"joy": 73},
        "British Shorthair Cat": {"famine": 25, "joy": 76},
        "Burmese cat": {"famine": 28,"joy": 80}}
class cat:
    def __init__(self, name):
        self.name=name
        self.gladness=50
        self.famine=50
        self.progress=50
        self.alive=True
    def to_eat(self):
        print("time to eat")
        self.progress+=1
        self.famine-=5
        self.gladness+=2.5
    def to_sleep(self):
        print("I will sleep")
        self.progress+=3
        self.gladness+=5
        self.famine+=2.5
    def to_chill(self):
        print("Rest time")
        self.progress+=0
        self.gladness+=5
        self.famine+=2.5
    def to_walk(self):
        print("I'm want walk")
        self.progress += 0
        self.gladness += 5
        self.famine += 2.5
    def to_play(self):
        print("I'm want play")
        self.progress += 0
        self.gladness += 5
        self.famine += 2.5
    def is_alive(self):
        if self.famine<+75:
            print("The cat died of hungrer..")
            self.alive=False
        elif self.gladness<=0:
            print("Depresion..")
            self.alive=False
        elif self.famine<100:
            print("The cat ate too much")
            self.alive=False
olena=Olena(name="Olena")
for day in range(1,8):
    if olena.live==False:
        break
    olena.live(day)