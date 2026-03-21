import random
def dungeon_name():
    adjectives=["Ancient","Whispering","Frozen","Burning","Cursed","Shattered","Hidden","Howling","Forgotten","Hollow","Sunken","Silent"]
    materials_or_traits=["Iron","Bone","Ash","Glass","Shadow","Storm","Ember","Ivory","Moss","Crystal","Steel","Smoke"]
    places=["Crypt","Cave","Tower","Ruins","Labyrinth","Fortress","Temple","Catacombs","Vault","Dungeon","Keep","Shrine"]
    
    random_input_one = random.choice(adjectives)
    random_input_two = random.choice(materials_or_traits)
    random_input_three = random.choice(places)

    print("The "+random_input_two+" "+random_input_three+" of the "+random_input_one+" Ones")
    
    
dungeon_name()

room_descriptions=["The air is cold and smells like wet stone.","Flickering torchlight reveals scratch marks on the wall.","You hear dripping water echoing far away.","The floor is cracked, and something shifts beneath it.","Strange symbols glow faintly on the ceiling.","A broken statue points toward a dark hallway.","The room is filled with thick fog that hugs the ground.","You step on bones that crunch underfoot.","The walls are warm, like something is breathing behind them.","A sudden gust blows out your light for a second."]
 
room_exploration = "y"

room_counter=0

randomizer=random.choice(room_descriptions)

monsters=["Dragon, danger level 5/5","Zombie, danger level 2/5","Skeleton, danger level 2.5/5","Green slime, danger level 1.5/5","Reaper, danger level 3.5/5","Evil mage, danger level 2.5/5","Evil spirit, danger level 4.5/5","Ghost, danger lavel 3.5"]

index=[]


while room_exploration != "n":

    room_counter=room_counter+1
    print("room number: "+str(room_counter))
    print(randomizer)
    monster_randomizer=random.choice(monsters)
    print("A monster in this room! It's a/an: "+monster_randomizer)
    if monster_randomizer not in index:
        print("New discovery! Added to the index")
        list(monster_randomizer)
        index="".join(monster_randomizer)
    elif monster_randomizer in index:
        print("Monster already discovered")

    room_exploration=input("continue exploring?(y/n): ")

    print(index)