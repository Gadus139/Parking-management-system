parking_records = []

def park_vehicle():
    plate = input("Enter vehicle plate number: ")
    owner = input("Enter owner name: ")
    parking_records.append({"plate": plate, "owner": owner})
    print("Vehicle parked successfully")

def view_parked_vehicles():
    if not parking_records:
        print("No vehicles parked")
    else:
        for record in parking_records:
            print("Plate:", record["plate"], "| Owner:", record["owner"])

def main():
    while True:
        print("1. Park Vehicle")
        print("2. View Parked Vehicles")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            park_vehicle()
        elif choice == "2":
            view_parked_vehicles()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
