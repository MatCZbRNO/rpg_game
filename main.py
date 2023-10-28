import fight
import create_characters


def even(num):
    if (num % 2) == 0:
        x = True
    else:
        x= False
    return x


pcCords=[12,11]
userCords=[3,3]
while True:
    char = input("\n Choose the class you want to play as: (w: warrior, m: mage, a: archer, 0: end the game) ")
    if char =="0":
        break
    else:
        cCH=create_characters.create(char)
        
        
        userStats= cCH[0] # power, defense, hp, actionsN, Adistance, maxHP
        pcStats = cCH[1] # power, defense, hp, actionsN, Adistance, maxHP, charPC
        
        userHp=userStats[2]
        pcHp=pcStats[2]
        
        while userStats[2] > 0 and pcStats[2] > 0:
            for i in range(userStats[3]+pcStats[3]):
                
                hps=fight.battle(userStats, char, pcStats[6], pcStats, pcStats[5], userCords, pcCords) # role, userStats, char, charPC, pcStats, maxHP, userCords, pcCords
            
                pcHp = hps[1]
                userHp = hps[0]
                
                userStats[2]=userHp
                pcStats[2]=pcHp
                
                cords=hps[2]
                
                userCords= cords[0]
                pcCords=cords[1]
                
                if pcHp <= 0 or userHp <= 0:
                    break
                
            if pcHp <= 0:
                print("\n\n\n\n          GAME OVER")
                print("\n   USER won the game!! \n\n\n\n")
                break
                
            elif userHp <= 0:
                print("\n\n\n\n          GAME OVER")
                print("\n   PC won the game!! \n\n\n\n")
                break
                
                    
                    

        #  attack(role, actions, distance, clas, pcAttacking, myHp, OpponentDefense, OpponentHp, OpponentPower):
