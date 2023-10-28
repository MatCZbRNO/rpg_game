import random
import mapa

def moveUser(userCords, pcCords, n):
    mapa.mapa(userCords, pcCords)
    print("You can take "+str(n)+" steps.")
    for i in range(n):     
        x = userCords[0]
        y = userCords[1]
        
        direction = input("Choose where to move (w: up, s: down, a: left, d: right, 0: stop): ")
        
        if direction.isnumeric() == True:
            if int(direction) == 0:
                break
            else:
                continue
        else:
            direction = direction.lower()
            if direction == "w":
                if y <= 0:
                    print("You can't go up.")
                    continue
                else:
                    y -= 1
                    
                    
            elif direction == "s":
                if y >= 14:
                    print("You can't go down.")
                    continue
                else:
                    y += 1
            elif direction == "a":
                if x <= 0:
                    print("You can't go left.")
                    continue
                else:
                    x -= 1
                    
                    
            elif direction == "d":
                if x >= 14:
                    print("You can't go right.")
                    continue
                else:
                    x += 1
        userCords=[x,y]
        
        mapa.mapa(userCords, pcCords)
            
    return [userCords, pcCords]
            

def movePC(userCords, pcCords, n, disPC, direction, Xokay, Yokay): # n - number of steps, r - USER or PC
    mapa.mapa(userCords, pcCords)
    for i in range(n):

        x = pcCords[0]
        y = pcCords[1]

        xPC = x
        yPC = y
        
        xUser = userCords[0]
        yUser = userCords[1]
         
        
        # distance check -------------------------------------------------------------------
        if Xokay == False:
            if direction == "a":
                x -= 1   
                    
            elif direction == "d":
                x += 1
                
            if xPC > xUser:
                if xPC - xUser <= disPC:
                    Xokay = True
                    break
                    
            elif xPC < xUser:
                if xUser - xPC <= disPC:
                    Xokay = True
                    break
            
        elif Yokay == False:
            if yPC > yUser:
                if yPC - yUser <= disPC:
                    Yokay = True
                    break
                
            elif yPC < yUser:
                if yUser - yPC <= disPC:
                    Yokay = True
                    break
            elif yPC == yUser:
                yOkay=True
                break
                
            if direction == "w":
                y -= 1
                    
            elif direction == "s":
                y += 1
    
        
        # moving ----------------------------------------------------------------------------------------------------

        pcCords=[x,y]
        
        mapa.mapa(userCords, pcCords)
    
    return [userCords, pcCords, Xokay, Yokay]


def awayPC(userCords, pcCords, n, direction): # n - number of steps, r - USER or PC
    for i in range(n):   
        x = pcCords[0]
        y = pcCords[1]
        
        if direction == "a":
            x -= 1   
                
        elif direction == "d":
            x += 1 
            
        elif direction == "w":
            y -= 1
                
        elif direction == "s":
            y = y+1
            
        pcCords[0]=x
        pcCords[1]=y
        
        mapa.mapa(userCords, pcCords)
    
    return [userCords, pcCords]