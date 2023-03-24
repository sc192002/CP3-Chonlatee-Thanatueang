usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "1234":
    print("<< Welcome to iShop >>")
    print("Menu Product iShop")
    print("1. Car        = 200 (THB)")
    car = ("Car")
    carPrice = 200
    print("2. Tank       = 500 (THB)")
    tank = ("Tank")
    tankPrice = 500
    print("3. Air Plane  = 900 (THB)")
    airPlane = ("Air Plane")
    airPlanePrice = 900
    print("4. Doll       = 100 (THB)")
    doll = ("Doll")
    dollPrice = 100
    print("Select iShop Product : ")
    custSelected = int(input(">> : "))
    if custSelected == 1:
        print(car)
        carInput = int(input("Qty Car : "))
        carTotal = (carPrice * carInput)
        print(car, " --Qty-- ", carInput, " Amount ", carTotal, "(THB)")
    elif custSelected == 2:
        print(tank)
        tankInput = int(input("Qty Tank : "))
        tankTotal = (tankPrice * tankInput)
        print(tank, " --Qty-- ", tankInput, " Amount ", tankTotal, "(THB)")
    elif custSelected == 3:
        print(airPlane)
        airPlaneInput = int(input("Qty Air Plane : "))
        airPlaneTotal = (airPlanePrice * airPlaneInput)
        print(airPlane, " --Qty-- ", airPlaneInput, " Amount ", airPlaneTotal, "(THB)")
    elif custSelected == 4:
        print(doll)
        dollInput = int(input("Qty Doll : "))
        dollTotal = (dollPrice * dollInput)
        print(doll, " --Qty-- ", dollInput, " Amount ", dollTotal, "(THB)")
else:
    print("Not found !")