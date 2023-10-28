import characters


def battle(userStats, char, charPC, pcStats, maxHP, userCords, pcCords):
    ATTACKNAMES = {"s": "sword", # sword
                   "sh": "shield", # shield
                   "b": "shadow ball", # shadow ball
                   "h": "heal", # heal
                   "a": "arrow", # normal arrow
                   "d": "dodge", # dodge
                   "m": "move", # move
                   "none": "error",
                   }
    ATTACKTYPES = {"s": 8, # sword
                   "sh": 5, # shield
                   "b": 7, # shadow ball
                   "h": 0, # heal
                   "a":7, # normal arrow
                   "d":4, # dodge
                   "m": 0, # move
                   }
    
    clas= char
    
    result=characters.attack(ATTACKNAMES, ATTACKTYPES, userStats, pcStats, maxHP, clas, charPC, userCords, pcCords) # hpUser, hpPC
    
    print("\nUSER: "+str(result[0])+" hp")
    print("PC: "+str(result[1])+" hp\n")
    
    return[result[0], result[1], result[2]]
                    


           
                
        
