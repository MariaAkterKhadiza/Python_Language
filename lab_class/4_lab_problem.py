#using super()
class Bird:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name, "makes a sound")

class Mannal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name, "makes a sound")

class Bat(Bird, Mannal):
    def __init__(self, name):
        super().__init__(name)

bat = Bat("Bat")
bat.speak()
