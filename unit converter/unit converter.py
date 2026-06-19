while True:
    print("\nUNIT CONVERTER TOOL")
    print("1. Length Converter")
    print("2. Weight Converter")
    print("3. Temperature Converter")
    print("4. Time Converter")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Length Converter
    if choice == "1":
        print("\nLENGTH CONVERTER")
        print("1. Meter to Kilometer")
        print("2. Kilometer to Meter")

        length_choice = input("Enter your choice: ")

        if length_choice == "1":
            meter = float(input("Enter meters: "))
            km = meter / 1000
            print("Kilometers:", km)

        elif length_choice == "2":
            km = float(input("Enter kilometers: "))
            meter = km * 1000
            print("Meters:", meter)

    # Weight Converter
    elif choice == "2":
        print("\nWEIGHT CONVERTER")
        print("1. Kilogram to Gram")
        print("2. Gram to Kilogram")

        weight_choice = input("Enter your choice: ")

        if weight_choice == "1":
            kg = float(input("Enter kilograms: "))
            gram = kg * 1000
            print("Grams:", gram)

        elif weight_choice == "2":
            gram = float(input("Enter grams: "))
            kg = gram / 1000
            print("Kilograms:", kg)

    # Temperature Converter
    elif choice == "3":
        print("\nTEMPERATURE CONVERTER")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")

        temp_choice = input("Enter your choice: ")

        if temp_choice == "1":
            celsius = float(input("Enter Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print("Fahrenheit:", fahrenheit)

        elif temp_choice == "2":
            fahrenheit = float(input("Enter Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print("Celsius:", celsius)

    # Time Converter
    elif choice == "4":
        print("\nTIME CONVERTER")
        print("1. Minutes to Hours")
        print("2. Hours to Minutes")

        time_choice = input("Enter your choice: ")

        if time_choice == "1":
            minutes = float(input("Enter minutes: "))
            hours = minutes / 60
            print("Hours:", hours)

        elif time_choice == "2":
            hours = float(input("Enter hours: "))
            minutes = hours * 60
            print("Minutes:", minutes)

    # Exit
    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")