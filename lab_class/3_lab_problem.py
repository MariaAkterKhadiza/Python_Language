  #only the method 
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
        Bird.__init__(self, name)
        Mannal.__init__(self, name)

bat = Bat("Bat")
bat.speak()
