def mapa(userCords, pcCords):
    for row in range(15):
        for col in range(15):
            if userCords[0] == col and userCords[1] == row:
                print("U", end=" ")
            elif pcCords[0] == col and pcCords[1] == row:
                print("P", end=" ")
            else:
                print(".", end=" ")
        print()
    print("\n--------------------------------------------------------------------------------------------------\n")