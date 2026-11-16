def calculate_force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s^2): "))
    force = mass * acceleration
    print("Force =", force, "N")

def calculate_kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    ke = 0.5 * mass * (velocity ** 2)
    print("Kinetic Energy =", ke, "J")

def calculate_potential_energy():
    mass = float(input("Enter mass (kg): "))
    height = float(input("Enter height (m): "))
    gravity = 9.8
    pe = mass * gravity * height
    print("Potential Energy =", pe, "J")




def calculate_ohms_law_voltage():
    current = float(input("Enter current (A): "))
    resistance = float(input("Enter resistance (Ohms): "))
    voltage = current * resistance
    print("Voltage =", voltage, "V")


def calculate_speed():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    if time == 0:
        print("Time cannot be zero")
    else:
        speed = distance / time
        print("Speed =", speed, "m/s")


def physics_operations():
    while True:
        print("\nChoose an operation (1-5):")
        print("1. Kinetic Energy")
        print("2. Force")
        print("3. Potential Energy")
        print("4. Voltage (Ohm's Law)")
        print("5. Speed")

        choice = input("Enter option (1-5): ")

        if choice == "1":
            calculate_kinetic_energy()
        elif choice == "2":
            calculate_force()
        elif choice == "3":
            calculate_potential_energy()
        elif choice == "4":
            calculate_ohms_law_voltage()
        elif choice == "5":
            calculate_speed()
        else:
            print("Not a valid option")

        again = input("\nDo you want to run another operation? (yes/no): ")
        if again != "yes":
            print("Program ended.")
            break


physics_operations()