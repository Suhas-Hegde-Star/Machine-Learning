while True:
    dest = int(input("Enter the distance to be traveled (in km): "))
    vehicle_type = input("Enter the vehicle type\n1. Car\n2. Bike\n3. Bus\n4. Luxury Car\n")

    if vehicle_type.lower() == "car" or vehicle_type == "1":
        vehicle = input("Enter the car type\n1. Hatchback\2. Sedan\n 3. SUV\n4. Crossoer\n5. Minivan\n6. Pickup Truck\n7.Coupe\n8. Convertable")
        if vehicle.lower == "hatchback" or vehicle == "1":
            comfort = 600
            milage = 24
        elif vehicle.lower() == "sedan" or vehicle == "2":
            comfort = 800
            milage = 19
        elif vehicle.lower() == "suv" or vehicle == "3":
            comfort = 850
            milage = 16
        elif vehicle.lower() == "crossover" or vehicle == "4":
            comfort = 750
            milage = 20
        elif vehicle.lower() == "minivan" or vehicle == "5":
            comfort = 900
            milage = 14
        elif vehicle.lower() == "pickup truck" or vehicle == "6":
            comfort = 500
            milage = 12
        elif vehicle.lower() == "coupe" or vehicle == "7":
            comfort = 650
            milage = 14
        elif vehicle.lower() == "convertable" or vehicle == "8":
            comfort = 670
            milage = 12
        else:
            print("Invalid Input")
    elif vehicle_type.lower() == "bike" or vehicle_type == "2":
        vehicle = input("Enter the bike type\n1. Standard\n2. Cruiser\n3. Touring\n4. Sport\n5. Adventure\n6. Dual Sport\n7. Scooter\n8. Off Road\n9. Sport Touring\n10. Electric")
        if vehicle.lower == "standard" or vehicle == "1":
            comfort = 700
            milage = 20
        elif vehicle.lower() == "cruiser" or vehicle == "2":
            comfort = 850
            milage = 15
        elif vehicle.lower() == "touring" or vehicle == "3":
            comfort = 950
            milage = 14 
        elif vehicle.lower() == "sport" or vehicle == "4":
            comfort = 650
            milage = 18
        elif vehicle.lower() == "adventure" or vehicle == "5":
            comfort = 800
            milage = 22
        elif vehicle.lower() == "dual sport" or vehicle == "6":
            comfort = 750
            milage = 25
        elif vehicle.lower() == "scooter" or vehicle == "7":
            comfort = 600
            milage = 30
        elif vehicle.lower() == "off road" or vehicle == "8":
            comfort = 500
            milage = 40
        elif vehicle.lower() == "sport touring" or vehicle == "9":
            comfort = 900
            milage = 16
        elif vehicle.lower() == "electric" or vehicle == "10":
            comfort = 820
            milage = 60
        else:
            print("Invalid Input")
    elif vehicle_type.lower() == "bus" or vehicle_type == "3":
        milage = 25
        comfort = 60
    elif vehicle_type.lower() == "luxury car" or vehicle_type == "4":
        milage = 20
        comfort = 95
    else:
        print()

    if vehicle_type == "bus":
        price = dest * milage
        f_price = price * comfort
        final_price = (f_price / 8) // 2
        print("The fare for the journey is: ₹", round(f_price, 0))
    elif vehicle_type == "car":
        price = dest * milage
        f_price = price * comfort
        final_price = (f_price / 16) // 10
        print("The fare for the journey is: ₹", round(f_price, 0))
    elif vehicle_type == "bike":
        price = dest * milage
        f_price = price * comfort
        final_price = (f_price / 16) // 15
        print("The fare for the journey is: ₹", round(f_price, 0))
    else:
        price = dest * milage
        f_price = price * comfort
        final_price = (f_price / 8) * 2
        print("The fare for the journey is: ₹", round(f_price, 0))