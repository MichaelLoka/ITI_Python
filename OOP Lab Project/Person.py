class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep (self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        elif hours > 7:
            self.mood = "Lazy"

    def eat (self, meals):
        if meals == 3:
            self.healthRate = "100%"
        elif meals == 2:
            self.healthRate = "75%"
        elif meals == 1:
            self.healthRate = "50%"

    def buy (self, items):
        if self.money >= items*10:
            self.money -= items*10
        else:
            print(f"You don't have enough money to buy {items} items")