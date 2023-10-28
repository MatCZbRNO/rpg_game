import movement


def percentage(number, amount): 
    z=(number/100) * amount
    print(" ") # +str(z)+" "+str(amount)+"%")
    return z

# pc direction ------------------------------------------------------------------------------------------------------------
def pcDirection(userCords, pcCords, stepsPC, disPC, Xokay, Yokay, away):
    
    xUser = userCords[0]
    yUser = userCords[1]
    
    xPC = pcCords[0]
    yPC = pcCords[1]
    
    
    if away == False:
        if xUser < xPC-disPC:
            direction = "a"
            Xokay=False
            
        elif xUser > xPC+disPC:
            direction = "d"
            Xokay=False
            
        elif yUser > yPC-disPC:
            direction = "s"
            Yokay=False
            
        elif yUser < yPC+disPC:
            direction = "w"
            Yokay=False
            
        moveO=movement.movePC(userCords, pcCords, stepsPC, disPC, direction, Xokay, Yokay)
        Xokay=moveO[2]
        Yokay=moveO[3]
            
    elif away == True:
        if xUser < xPC-disPC:
            direction = "a"
            
        elif xUser > xPC+disPC:
            direction = "d"
            
        elif yUser > yPC-disPC:
            direction = "s"
            
        elif yUser < yPC+disPC:
            direction = "w"
        
        moveO=movement.awayPC(userCords, pcCords, stepsPC, direction)
    
    c=[moveO[0], moveO[1]]
    return c

# distance check ------------------------------------------------------------------------------------------------------------
def distanceCHECK(xUser,yUser,disUser,xPC,yPC,disPC,role):
    okay = False
    
    if role == "USER":
        if xPC > xUser and yPC > yUser:
            if xPC-xUser <= disUser and yPC - yUser <= disUser:
                okay = True
            if xPC-xUser > disUser and yPC - yUser > disUser:  
                okay = False
            
        if xPC < xUser and yPC < yUser:
            if xUser - xPC <= disUser and yUser - yPC <= disUser:
                okay = True
            if xUser - xPC > disUser and yUser - yPC > disUser:
                okay = False
        return okay
                
    if role == "PC":
        if xPC < xUser and yPC < yUser:
            if xUser - xPC <= disPC and yUser - yPC <= disPC:
                okay = True
            if xUser - xPC > disPC and yUser - yPC > disPC:                  
                okay = False
            
        if xPC > xUser and yPC > yUser:
            
            if xPC-xUser <= disPC and yPC - yUser <= disPC:
                okay = True
            if xPC-xUser > disPC and yPC - yUser > disPC:
                okay = False
                
        return okay

# attack -----------------------------------------------------------------------------------------------------------------------------------------
def attack(ATTACKNAMES, ATTACKTYPES, userStats, pcStats, maxHP, clas, clasPC, userCords, pcCords):
    Xokay=None
    Yokay=None
     # power, defense, hp, actionsN, Adistance
    hpUser = userStats[2]
    defenseUser = userStats[1]
    powerUser = userStats[0]
    disUser = userStats[4]
    stepsUser = userStats[3]
    xUser = userCords[0]
    yUser = userCords[1]
    
    
    defensePC = pcStats[1]
    hpPC = pcStats[2]
    powerPC = pcStats[0]
    disPC = pcStats[4]
    stepsPC = pcStats[3]
    xPC = pcCords[0]
    yPC = pcCords[1]

    # choosing attacks             
    c = [userCords,pcCords]
    
    if clas == "a":
        ATTACKtype = input("Choose, what you want to do: (a: arrow, d: dodge, m: move) ")
            
    elif clas == "w":
        ATTACKtype = input("Choose, what you want to do: (s: sword, sh: shield, m: move) ")
            
    elif clas == "m":
        ATTACKtype = input("Choose, what you want to do: (b: shadow ball, h: heal, m: move) ")
    
    disOK = distanceCHECK(xUser,yUser,disUser,xPC,yPC,disPC,"PC")
    ATTACKtypePC = "none"
    
    if disOK == True:
        # pc has archer class -----------------------------------------------------------------------------------------------------
        if clasPC=="a":
            if hpPC <= percentage(maxHP, 30) and hpPC >= percentage(maxHP, 26):
                ATTACKtypePC = "d"
                
            elif hpPC >= percentage(maxHP, 60) or hpPC <= percentage(maxHP, 25):
                ATTACKtypePC = "a"
                
            elif hpPC <= percentage(maxHP,50) and hpPC >= percentage(maxHP, 30):
                ATTACKtypePC = "m"
                c=pcDirection(userCords, pcCords, stepsPC, disPC, Xokay, Yokay, True)
            else:
                ATTACKtypePC = "a"
                
        # pc has warrior class -----------------------------------------------------------------------------------------------------        
        elif clasPC == "w":
            if hpPC <= percentage(maxHP, 30) and hpPC >= percentage(maxHP, 26):
                ATTACKtypePC = "sh"
                
            elif hpPC <= percentage(maxHP, 25):
                ATTACKtypePC = "s"
                
            elif hpPC <= percentage(maxHP,50) and hpPC >= percentage(maxHP, 30):
                ATTACKtypePC = "m"
                c=pcDirection(userCords, pcCords, stepsPC, disPC, Xokay, Yokay, True)
            else:
                ATTACKtypePC = "s"
              
                
        # pc has mage class -----------------------------------------------------------------------------------------------------        
        elif clasPC == "m":
            if hpPC <= percentage(maxHP, 30) and hpPC >= percentage(maxHP, 26):
                ATTACKtypePC = "h"
                
            elif hpPC >= percentage(maxHP, 60) or hpPC <= percentage(maxHP, 25):
                ATTACKtypePC = "b"
                
            elif hpPC <= percentage(maxHP,50) and hpPC >= percentage(maxHP, 30):
                ATTACKtypePC = "m"
                c=pcDirection(userCords, pcCords, stepsPC, disPC, Xokay, Yokay, True)
            else:
                ATTACKtypePC = "b"
            
    else:
        ATTACKtypePC = "m"
        c=pcDirection(userCords, pcCords, stepsPC, disPC, Xokay, Yokay, False)
        

    
    print("USER used "+ATTACKNAMES.get(ATTACKtype))
    print("PC used "+ATTACKNAMES.get(ATTACKtypePC))
    
    defend=["d","sh","h","m"]
    offend=["s","a","b"]
    
    if ATTACKtype=="m":
        c=movement.moveUser(c[0], c[1], stepsUser)
    
    elif ATTACKtype == "h":
        hpUser += 15
    elif ATTACKtypePC == "h":
        hpPC += 15
    
    # both defend ------------------------------------------------------------------------------------------
    
    if ATTACKtype in defend and ATTACKtypePC in defend:
        pass
    
    # only user offends -----------------------------------------------------------------------------------
    
    elif ATTACKtype in offend and ATTACKtypePC in defend: 
        disOK = distanceCHECK(xUser,yUser,disUser,xPC,yPC,disPC,"USER")
            
        if disOK == True:
            hpPC -= ATTACKTYPES.get(ATTACKtype) *2 - defensePC
        else:
            print("USER isn' t close enough to attack PC.")
    
    # only pc offends -------------------------------------------------------------------------------------
    
    elif ATTACKtype in defend and ATTACKtypePC in offend: 
        hpUser -= ATTACKTYPES.get(ATTACKtypePC) *2 - defenseUser

    
    # both offend -----------------------------------------------------------------------------------------
    
    elif ATTACKtype in offend and ATTACKtypePC in offend:
        hpUser -= ATTACKTYPES.get(ATTACKtypePC)
#         print(str(ATTACKTYPES.get(ATTACKtypePC)))
        
        disOK = distanceCHECK(xUser,yUser,disUser,xPC,yPC,disPC,"USER")
        
#         print(str(disOK))
        
        if disOK == True:
            hpPC = hpPC - ATTACKTYPES.get(ATTACKtype)
        else:
            print("USER isn' t close enough to attack PC.")
            


    return[hpUser, hpPC, c]