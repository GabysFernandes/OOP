class SuperHero:
 
    def __init__(self, name="", alias="", special_skill=""):
        self.name = name
        self.alias = alias
        self.special_skill = special_skill

    def __str__(self):

        return f"{self.name}: {self.alias} - {self.special_skill}"