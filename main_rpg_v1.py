from random import choice
import random

def mapa(userCords, pcCords):
  for row in range(10):
    for col in range(10):
      if userCords[0] == col and userCords[1] == row:
        print("U", end=" ")
      elif pcCords[0] == col and pcCords[1] == row:
        print("P", end=" ")
      else:
        print(".", end=" ")
    print()

def warrior(user, pc):
  ACTIONS = {"s": 5,
             "sh": 10,
            }
  
  action = input("Zvolte akci, kterou chcete udělat: (s: sword, sh: shield) ")
  if action in ACTIONS.keys():
    if action == "s" or action == "sh":
      if action == "s":
        pc[2] -= ACTIONS.get("s") *2 - pc[1]
      elif action == "sh":
        user[2] -= pc[0] *2 - ACTIONS.get("sh")
      else:
        print("Tato postava nemůže provést tuto akci.")
    else:
      print("Tato akce neexistuje")

def mage(user, pc):
  ACTIONS = {"b": 10,
             "sh": 10,
             "h": 10,
            }
  action = input("Zvolte akci, kterou chcete udělat: (b: shadowball,sh: magic shield, h: heal 10) ")
  if action in ACTIONS.keys():
    if action == "b" or action == "sh" or action == "h":
      if action == "b":
        pc[2] -= ACTIONS.get("b") *2 - pc[1]
      elif action == "sh":
        user[2] -= pc[0] *2 - ACTIONS.get("sh")
      elif action == "h":
        user[2] += 10
      else:
        print("Tato postava nemůže provést tuto akci.")
    else:
      print("Tato akce neexistuje")

def archer(user, pc):
  ACTIONS = {"n": 5,
             "f": 7,
             "d": 3,
            }
  action = input("Zvolte akci, kterou chcete udělat: (n: normal arrow, f: fire arrow, d: defend) ")
  if action in ACTIONS.keys():
    if action == "n" or action == "f" or action == "d":
      if action == "n":
        pc[2] -= ACTIONS.get("n") *2 - pc[1]
      elif action == "f":
        pc[2] -= ACTIONS.get("f") *2 - pc[1]
      elif action == "d":
        user[2] -= pc[0] *2 - ACTIONS.get("d")
    else:
      print("Tato postava nemůže provést tuto akci.")
  else:
    print("Tato akce neexistuje")

def mCh(characterClass): 
    # mCh > make character
    output= []
    
    if characterClass == "w":
        power = 5
        defense = 10
        health = 150
        return[power, defense, health, characterClass]
        
    elif characterClass == "m":
        power = 10
        defense = 3
        health = 70
        return[power, defense, health, characterClass]

        
    elif characterClass == "a":
        power = 7
        defense = 4
        health = 100
        return[power, defense, health, characterClass]      

    return output

def fight(user,pc):
    ACTIONS = {"s": 5,
               "sh": 10,
               "b": 10,
               "h": 10,
               "n": 5,
               "f": 7,
               "d": 3,
               }

    #print(ACTIONS.get("s"))
    # cyklus pro jednotilvý kola, opakuje se dokud oba žijí
    

    while user[2] >0 and pc[2]>0:
        # user utoci - pc brani
        print("map:")
        userCords= [1, 1]
        pcCords= [9,9]
        mapa(userCords, pcCords)
        if user[3] == "w":
          warrior(user, pc)
        elif user[3] == "m":
          mage(user, pc)     
        elif user[3] == "a":
          archer(user, pc)
          print(f"USER: {userChar}")
          print(f"PC: {pcChar}")
          # pc utoci - user brani
          if pc[3] == "w":
              action = random.randint(1,2)
              if action == 1:
                  user[2] -= ACTIONS.get("s") *2 - user[1]
              elif action == 2:
                  pc[2] -= user[0] *2 - ACTIONS.get("sh")
              else:
                  print("Tato postava nemůže provést tuto akci.")
          elif pc[3] == "m":
              action = random.randint(1,3)
              if action == 1:
                  user[2] -= ACTIONS.get("b") *2 - user[1]
              elif action == 2:
                  pc[2] -= user[0] *2 - ACTIONS.get("sh")
              elif action == 3:
                  pc[2] += 10
          else:
              print("Tato postava nemůže provést tuto akci.")
        elif pc[3] == "a":
            action = random.randint(1,3)
            if action == "n":
                pc[2] -= ACTIONS.get("n") *2 - pc[1]
            elif action == "f":
                pc[2] -= ACTIONS.get("f") *2 - pc[1]
            elif action == "d":
                user[2] -= pc[0] *2 - ACTIONS.get("d")
            else:
                print("Tato postava nemůže provést tuto akci.")


    print(f"USER: {userChar}")
    print(f"PC: {pcChar}")

        
    # vrati vítěze
    if user[2] > 0:
        print("vyhrál jsi")
    else:
        print("prohrál jsi")


print("Hello in my game")

while True:
    # vytvořit hráčovu postavu
    clas = input("Zvol si třídu, jakou chceš hrát: (w: warrior, m: mage, a: archer, 0: ukončení hry) ")
    userChar= mCh(clas)
    if clas == "0":
        break
    # vytvořit nepřítele
    pcChar = mCh(choice(["w", "m", "a"]))
    
    print(" PC/USER: power, defense, health, class")
    
    print(f"USER: {userChar}")
    print(f"PC: {pcChar}")
    # souboj
    fight(userChar, pcChar)
    # vyhodnocení

