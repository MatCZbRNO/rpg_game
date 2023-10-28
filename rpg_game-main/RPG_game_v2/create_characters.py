import random

# charakters (role, attack power, defense, hp, number of actions, attack distance)

class Character:
    def __init__(self, role, myPower, myDefense, myHp, actions, distance, OpponentPower, OpponentDefense, OpponentHp, clas):
        self.OpponentPower=OpponentPower # opponents attack power, integer
        self.OpponentDefense = OpponentDefense # opponents defense, integer
        self.OpponentHp=OpponentHp # opponents hp, integer
        
        self.role=role # string, names of roles, example: "PC" and "USER"
        self.clas=clas
        
        self.actions=actions # your number of actions, integer
        self.distance=distance # your attack distance, integer
        self.myPower=myPower # my attack power, integer
        self.myDefense=myDefense # my defense, integer
        self.myHp=myHp # my hp, integer
    
    def stats(self):
        print(self.role+"s stats: ", end=" ")
        if self.role == "PC":
            print(str(self.myPower)+" power\n            "+str(self.myDefense)+" defense\n            "+str(self.myHp)+" hp\n            "+str(self.distance)+" attack distance\n            "+self.clas)
        elif self.role == "USER":
            print(str(self.myPower)+" power\n              "+str(self.myDefense)+" defense\n              "+str(self.myHp)+" hp\n              "+str(self.distance)+" attack distance\n              "+self.clas)

def create(char):  
   # user chooses character
    userStats=[]
    pcStats=[]
    CHARACTERS={"w": "warrior",
                "m": "mage",
                "a": "archer",}
    if char in ["w", "m", "a"]:
        if char == "w":
            power=8
            defense=5
            hp=150
            maxHP=150
            actionsN=5
            Adistance=1
            
            
        elif char == "m":
            power=7
            defense=0
            hp=80
            maxHP=80
            actionsN=3
            Adistance=3
            
            
        elif char == "a":
            power=7
            defense=4
            hp=40
            maxHP=40
            actionsN=2
            Adistance=6
            
        userStats=[power, defense, hp, actionsN, Adistance, maxHP]
            
        
    else:
        print("Not existing character"+"\n")

    # pc chooses character
    charPC = random.choice(["w", "m", "a"])
    if charPC == "w":     # role, power, defense, hp, steps, aDistance, opponent power, opponent defense, class
        CharPC= Character("PC", 8, 5, 150, 5, 1, userStats[0], userStats[1], userStats[2], CHARACTERS.get(charPC)) 
        pcStats=[8,5,150, 5, 1, 150, charPC] # power, defense, hp, steps, aDistance, max hp, class
        
    elif charPC == "m":  # role, power, defense, hp, steps, aDistance, opponent power, opponent defense, class
        CharPC= Character("PC", 7, 0, 80, 3, 3, userStats[0], userStats[1], userStats[2], CHARACTERS.get(charPC))
        pcStats=[7,0,80, 3, 3, 80, charPC] # power, defense, hp, steps, aDistance, max hp, class
        
    elif charPC == "a":  # role, power, defense, hp, steps, aDistance, opponent power, opponent defense, class
        CharPC= Character("PC", 7, 4, 40, 2, 6, userStats[0], userStats[1], userStats[2], CHARACTERS.get(charPC))
        pcStats=[7,4,40,2,6, 40, charPC] # power, defense, hp, steps, aDistance, max hp, class
    
    CharUSER= Character("USER", power, defense, hp, actionsN, Adistance, pcStats[0], pcStats[1], pcStats[2], CHARACTERS.get(char))
                       # role, power, defense, hp, steps, aDistance, opponent power, opponent defense, class
    print(CharPC.stats())
    print(CharUSER.stats())
    
    return[userStats, pcStats]

    