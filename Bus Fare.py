# bus standard fare calculator

def calculate_bus_fare(age):
    standard_fare = (int(input("Enter the standard bus fare: "))) 
    "Calculates bus fare based on age."
    if age < 1-2:
        return 0  # Free for infants between ages 1 and 2
    elif age < 3-7:
        return 5  # Discount for toddlers between ages 3 and 7
    elif age < 8-12:
        return 10 # Discount for preteens between ages 8 and 12
    elif age < 13-19:
        return 16  # Discount for teenagers between ages 13 and 19
    elif age < 20-39:
        return 30  # Standard fare for younger adults between ages 20 and 39
    elif age < 40-59:
        return 50  # Standard fare for middle-aged adults between ages 40 and 59
    elif age < 60-79:
        return 15  # Discount for older adults between ages 60 and 79
    elif age < 80-99:
        return 10  # Discount for elderly seniors between ages 80 and 99
    else:
        return standard_fare # Get standard fare input from the user 

# Get Example Usage Input from the User
try:
    passenger_age = int(input("Enter passenger age: "))
    bus_fare = calculate_bus_fare(passenger_age)
    print(f"The bus fare is: ${bus_fare:.2f}")
except ValueError:
        print("Invalid input. Please enter a valid standard bus fare.")
        print("Invalid input. Please enter a valid age number.")
        print("Exiting the program.")
