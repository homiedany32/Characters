

class Character():
    def __init__(self):
        super().__init__()
        self.name = ""
        self.phrase = ""
        self.phrase2 = ""
        self.level = 1

    def speak(self, phraseNum):
        if  phraseNum == 1:
            print(self.phrase)
        elif  phraseNum == 2:
            print(self.phrase2)

    def setLevel(self, newLevel):
        self.level = newLevel
        print(self.name + " is now at level " + str(self.level))

Bilbo = Character()
Bilbo.name = "Bilbo"
Bilbo.phrase = "Sorry, I Don't Want Any Adventures Today. Thank You!"
Bilbo.phrase2 = "I'm Going On An Adventure!"
Bilbo.level = 1

Frodo = Character()
Frodo.name = "Frodo"
Frodo.phrase = "There Is No Real Going Back."
Frodo.phrase2 = "I Will Take The Ring, Though I Do Not Know The Way."
Frodo.level = 1


Bilbo.speak(1)
Bilbo.setLevel(2)
Bilbo.speak(2)
