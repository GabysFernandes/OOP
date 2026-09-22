from app_data import AppData
from abstract_demo import Dog, Cat, LandBird, FlyBird, Wolf
from heroes import HumanHero, Batman, SpiderMan


print(AppData.APP_VERSION)

dog = Dog("Alfie")
cat = Cat("Bianca")
dog1 = Dog("Fido")
wolf = Wolf("Scott")

brian = LandBird("Brian")
fly_bird = FlyBird("Sky")

print(f"dog {dog.describe()}")
print(f"cat {cat.describe()}")
print(f"bird {brian.describe()}")
print(f"Brian Jumps {brian.jump()}")
print(f"Sky Jumps {fly_bird.jump()}")
print(f"cat Jumps {cat.jump()}")
print(f"wolf {wolf.describe()}")

human_hero = HumanHero()

batman = Batman()

batman.fly()
batman.land()

spiderMan = SpiderMan()

spiderMan.sling()