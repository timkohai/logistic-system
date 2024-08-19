import re
from datetime import datetime


# Added a comment

# TODO: Move all regex expression in a class
# Regex Pattern
# Vehicle ID: e.g., V001
VEHICLE_ID_FORMAT = r'^V\d{3}$'

# Customer ID: e.g., C-001
CUSTOMER_ID_FORMAT = r'^C-\d{3}$'

# Shipment ID: e.g., S001
SHIPMENT_ID_FORMAT = r'^S\d{3}$'

# Address: e.g 10 Sunnyoaks Lane, VIC 2001
ADDRESS_FORMAT = r'^[\w\s]+,\s*(NSW|VIC|QLD|SA|WA|TAS|NT|ACT)\s*\d{4}$'

# Phone: 04XXXXXXXX
PHONE_FORMAT = r'^04\d{8}$'

# Email: customer@email.com
EMAIL_FORMAT = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hi I am", self.name)


class Engineer(Employee):
    def last_name(self):
       print("Test") 


# Instance of Employee
david = Employee("David", 30)
tshering = Employee("Tshering", 28)


















class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, vehicle_capacity):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.vehicle_capacity = vehicle_capacity

    def to_list(self):
        return [self.vehicle_id, self.vehicle_type, self.vehicle_capacity]

    def preview(self):
        return f"Vehicle ID: {self.vehicle_id}, Type: {self.vehicle_type}, Capacity: {self.vehicle_capacity} kg"

class Customer:
    def __init__(self, customer_id, name, dob, address, phone, email):
        self.customer_id = customer_id
        self.name = name
        self.__dob = dob
        self.address = address
        self.__phone = phone
        self.email = email

    def get_phone(self):
        return self.__phone
    
    def set_phone(self, phone):
        self.__phone = phone

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob

    def to_list(self):
        return [self.customer_id, self.name, self.__dob, self.address, self.__phone, self.email]

class Shipment:
    def __init__(self, shipment_id, customer_id, origin, destination, weight, vehicle_id):
        self.shipment_id = shipment_id
        self.customer_id = customer_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.vehicle_id = vehicle_id
        self.status = "In Transit"
        self.delivery_date = None
        self.delivery_time = None

    def to_list(self):
        return [self.shipment_id, self.customer_id, self.origin, self.destination, self.weight, 
                self.vehicle_id, self.status, self.delivery_date, self.delivery_time]


class BaseManagement:
    def __init__(self):
        pass

    def display_tabular_records(self, headers, data):
        # Calculate column widths dynamically
        column_widths = [max(len(str(item)) for item in col) for col in zip(headers, *data)]
        width = sum(column_widths) + len(headers) * 3 + 1

        # Print table header
        print('-' * width)
        print("| " + " | ".join(f"{header:<{column_widths[i]}}" for i, header in enumerate(headers)) + " |")
        print('-' * width)

        # Print table data
        for row in data:
            print("| " + " | ".join(f"{str(item):<{column_widths[i]}}" for i, item in enumerate(row)) + " |")
        print('-' * width)

class FleetManagement(BaseManagement):
    def __init__(self):
        self.vehicles = [Vehicle("V001", "Truck", 5000), Vehicle("V002", "Van", 2000)]

    def get_available_vehicles(self):
        return self.vehicles

    def add_vehicle(self):
        # Get a valid vehicle ID from the user
        vehicle_id = self.get_valid_vehicle_id()
        if not vehicle_id:
            return

        # Get vehicle type from the user
        vehicle_type = input("Enter Vehicle Type (e.g., Truck, Van, Car): ")

        # Get a valid vehicle_capacity from the user
        vehicle_capacity = self.get_valid_capacity()
        if not vehicle_capacity:
            return

        # Create and add the new vehicle to the fleet
        new_vehicle = Vehicle(vehicle_id, vehicle_type, vehicle_capacity)
        self.vehicles.append(new_vehicle)
        print(f"\nVehicle {vehicle_id} added successfully.")

    def update_vehicle(self):
        # Get the vechile ID to update
        vehicle_id = input("\nEnter the Vehicle ID of the vehicle you want to update: ")
        vehicle = self.find_vehicle(vehicle_id)

        if vehicle:
            # Display current vehicle information
            print(f"Current vehicle information:\n  {vehicle.preview()}")

            # Update vehicle type if new input is provided
            new_type = input("Enter new Vehicle Type (or press Enter to keep current): ")
            if new_type:
                vehicle.vehicle_type = new_type

            # Update vehicle capacity if valid input is provided
            new_capacity = self.get_valid_capacity()
            if new_capacity:
                vehicle.vehicle_capacity = new_capacity

            print(f"\nVehicle {vehicle_id} updated successfully.\n New information: {vehicle.preview()}")
        else:
            print(f"\nVehicle ID {vehicle_id} not found.")

    def remove_vehicle(self):
        # Get the vehicle ID to remove
        vehicle_id = input("Enter the Vehicle ID of the vehicle you want to remove: ")
        vehicle = self.find_vehicle(vehicle_id)

        if vehicle:
            # Display vehicle information and confirm removal
            print(f"Vehicle found: {vehicle.preview()}")
            confirmation = input("Are you sure you want to remove this vehicle? (yes/no): ").lower()

            if confirmation == 'yes':
                self.vehicles.remove(vehicle)
                print(f"Vehicle {vehicle_id} has been successfully removed from the fleet.")
            else:
                print(f"Vehicle removal cancelled.")
        else:
            print(f"Vehicle ID {vehicle_id} not found")

    def view_all_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.")
            return

        while True:
            # Display all vehicles in a tabular format
            headers = ["ID", "Type", "Capacity (kg)"]
            data = [vehicle.to_list() for vehicle in self.vehicles]

            print("\nAll Vehicles in the Fleet:")
            self.display_tabular_records(headers, data)

            # Calculate and display fleet statistics
            total_vehicles = len(self.vehicles)
            print(f"Total vehicles: {total_vehicles}")

            # Allow users to exit to previous menu
            command = input("\nType 'exit' to return to the previous menu: ").lower()
            if command == 'exit':
                break;

    def get_valid_vehicle_id(self):
        while True:
            vehicle_id = input("Enter Vehicle ID (format: V followed by 3 digitas, e.g., V001): ")
            # Validate vehicle ID format using regex
            if not re.match(VEHICLE_ID_FORMAT, vehicle_id):
                print("Invalid Vehicle ID format. Please use 'V' followed by 3 digits.")
                continue
            # Check for uniqueness of vehicle ID
            if any(vehicle.vehicle_id == vehicle_id for vehicle in self.vehicles):
                print("Vehicle ID already exists. Please enter a unique ID.")
                continue
            return vehicle_id

    def get_valid_capacity(self):
        while True:
            capacity = input("Enter Vehicle Capacity (in kg): ")
            try:
                capacity = int(capacity)
                # Ensure capacity is positive
                if capacity <= 0:
                    print("Invalid input. Capacity must be a positive integer.")
                    continue
                return capacity
            except ValueError:
                print("Invalid input. Capacity must be a positive integer.")

    def find_vehicle(self, vehicle_id):
        # Iterate through the vehicles list to find vehicle by ID
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None

        

    def menu(self):
        while True:
            print("\n")
            print("-" * 20)
            print("| Fleet Management Menu:")
            print("-" * 20)
            print("1. Add a vehicle")
            print("2. Update vehicle information")
            print("3. Remove a vehicle")
            print("4. View all vehicles")
            print("5. Quit fleet management")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_vehicle()
            elif choice == '2':
                self.update_vehicle()
            elif choice == '3':
                self.remove_vehicle()
            elif choice == '4':
                self.view_all_vehicles()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")


class CustomerManagement(BaseManagement):
    def __init__(self, shipment_management):
        # Initialize with sample customers
        self.customers = [
            Customer("C-001", "Timothy", "28/05/1989", "3 Sunnyoaks Lane, VIC 2000", "0449153950", "britonetmu@gmail.com"),
            Customer("C-002", "John", "02/02/1990", "3 Manga Lane, NSW 2000", "0449153951", "john@gmail.com"),
            Customer("C-003", "Doe", "12/03/1991", "3 Hinog Lane, QLD 2000", "0449153952", "doe@gmail.com")
        ]
        self.shipment_management = shipment_management

    def add_customer(self):
        # Get valid customer ID
        customer_id = self.get_valid_customer_id()
        if not customer_id:
            return

        # Get customer name
        name = input("Enter customer name: ")

        # Get valid date of birth
        dob = self.get_valid_dob()
        if not dob:
            return

        # Get valid address
        address = self.get_valid_address()
        if not address:
            return

        # Get valid phone number
        phone = self.get_valid_phone()
        if not phone:
            return

        # Get valid email
        email = self.get_valid_email()
        if not email:
            return

        # Create new customer and add to list
        new_customer = Customer(customer_id, name, dob, address, phone, email)
        self.customers.append(new_customer)

        print(f"Customer {customer_id} added successfully.")

    def update_customer(self):
        customer_id = input("Enter the Customer ID of the customer you want to update: ")

        customer = self.find_customer(customer_id)
        if not customer:
            print("Error: Customer not found.")
            return

        print(f"Updating information for customer: {customer.name} (ID: {customer.customer_id})")

        # Update customer information
        customer.name = input(f"Enter new name (current: {customer.name}): ") or customer.name
        new_dob = self.get_valid_dob(current=customer.get_dob())
        customer.set_dob(new_dob)
        customer.address = self.get_valid_address(current=customer.address)
        new_phone = self.get_valid_phone(current=customer.get_phone())
        customer.set_phone(new_phone)
        customer.email = self.get_valid_email(current=customer.email)

        print(f"Customer {customer_id} updated successfully.")

    def remove_customer(self):
        customer_id = input("Enter the Customer ID of the customer you want to remove: ")

        customer = self.find_customer(customer_id)
        if not customer:
            print("Error: Customer not found.")
            return

        print(f"Customer found: {customer.name} (ID: {customer.customer_id})")
        print(f"Address: {customer.address}")
        print(f"Phone: {customer.phone}")
        print(f"Email: {customer.email}")

        confirmation = input("Are you sure you want to remove this customer? (yes/no): ").lower()

        if confirmation == 'yes':
            self.customers.remove(customer)
            print(f"Customer {customer_id} has been successfully removed.")
        else:
            print("Customer removal cancelled.")

    def view_all_customers(self):
        if not self.customers:
            print("No customers in the system.")
            return

        while True:
            headers = ["ID", "Name", "Date of Birth", "Address", "Phone", "Email"]
            data = [customer.to_list() for customer in self.customers]

            print("\nAll Customers:")
            self.display_tabular_records(headers, data)

            print(f"\nTotal customers: {len(self.customers)}")

            command = input("\nType 'exit' to return to the previous menu: ").lower()
            if command == 'exit':
                break

    def view_customer_shipments(self):
        customer_id = input("Enter the Customer ID to view shipments: ")

        customer = self.find_customer(customer_id)
        if not customer:
            print("Error: Customer not found. Please check the Customer ID and try again.")
            return

        shipments = self.shipment_management.get_customer_shipments(customer_id)
        if not shipments:
            print(f"No shipments found for Customer {customer_id}.")
            return

        headers = ["Shipment ID", "Origin", "Destination", "Weight", "Vehicle ID", "Status", "Delivery Date"]
        data = [[s.shipment_id, s.origin, s.destination, s.weight, s.vehicle_id, s.status, s.delivery_date or "N/A"] 
                for s in shipments]

        print(f"\nShipments for Customer {customer_id}:")
        self.display_tabular_records(headers, data)

    def get_valid_customer_id(self):
        while True:
            customer_id = input("Enter Customer ID (format: C-XXX, where X is a digit): ")
            if not re.match(CUSTOMER_ID_FORMAT, customer_id):
                print("Error: Invalid Customer ID format. Please use C-XXX format where X is a digit")
                continue
            if any(customer.customer_id == customer_id for customer in self.customers):
                print("Error: Customer ID already exists. Please enter a unique ID.")
                continue
            return customer_id
    
    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def get_valid_dob(self, current=None):
        while True:
            dob = input(f"Enter date of birth (DD/MM/YYYY) (current: {current}): ") or current
            try:
                dob_date = datetime.strptime(dob, "%d/%m/%Y")
                age = (datetime.now() - dob_date).days // 365
                if age < 18:
                    print("Error: Customer must be at least 18 years old.")
                    continue
                return dob
            except ValueError:
                print("Error: Invalid date format. Please use DD/MM/YYYY")

    def get_valid_address(self, current=None):
        while True:
            address = input(f"Enter address (current: {current}): ") or current
            if re.match(ADDRESS_FORMAT, address, re.IGNORECASE):
                return address
            print("Error: Invalid address format. Please enter: Street, State Postcode")
            print("Example: 123 Main St, NSW 2000")

    def get_valid_phone(self, current=None):
        while True:
            phone = input(f"Enter phone number (format: 04XXXXXXXX) (current: {current}): ") or current
            if re.match(PHONE_FORMAT, phone):
                return phone
            print("Error: Invalid phone number. Please use the format 04XXXXXXXX.")

    def get_valid_email(self, current=None):
        while True:
            email = input(f"Enter email address: (current: {current}): ") or current
            if re.match(EMAIL_FORMAT, email):
                return email
            print("Error: Invalid email address. Please enter a valid email.")

    def menu(self):
        while True:
            print("\n")
            print("-" * 20)
            print("| Customer Management Menu:")
            print("-" * 20)
            print("1. Add a customer")
            print("2. Update customer information")
            print("3. Remove a customer")
            print("4. View all customers")
            print("5. View a customer's shipments")
            print("6. Quit Customer Management")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_customer()
            elif choice == '2':
                self.update_customer()
            elif choice == '3':
                self.remove_customer()
            elif choice == '4':
                self.view_all_customers()
            elif choice == '5':
                self.view_customer_shipments()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

class ShipmentManagement(BaseManagement):
    def __init__(self, fleet_management, customer_management):
        # Initialize with a sample shipment
        self.shipments = [
            Shipment("S001", "C-001", "Sydney", "Melbourne", 100, "V001")
        ]
        self.fleet_management = fleet_management
        self.customer_management = customer_management

    def create_shipment(self):
        # Get valid shipment ID
        shipment_id = self.get_valid_shipment_id()
        if not shipment_id:
            return

        # Get valid customer ID
        customer_id = self.get_valid_customer_id()
        if not customer_id:
            return

        # Get origin and destination
        origin = input("Enter origin location: ")
        destination = input("Enter destination location: ")

        # Get valid weight
        weight = self.get_valid_weight()
        if weight is None:
            return

        # Get valid vehicle ID
        vehicle_id = self.get_valid_vehicle_id()
        if not vehicle_id:
            return

        # Create new shipment and add to list
        new_shipment = Shipment(shipment_id, customer_id, origin, destination, weight, vehicle_id)
        self.shipments.append(new_shipment)

        print(f"Shipment {shipment_id} created successfully.")

    def track_shipment(self):
        shipment_id = input("Enter the Shipment ID you want to track: ")

        shipment = self.find_shipment(shipment_id)
        if not shipment:
            print("Error: Shipment not found. Please check the Shipment ID and try again.")
            return

        print(f"\nShipment {shipment_id} Status: {shipment.status}")
        print(f"Origin: {shipment.origin}")
        print(f"Destination: {shipment.destination}")
        print(f"Weight: {shipment.weight} kg")
        print(f"Vehicle ID: {shipment.vehicle_id}")
        if shipment.status == "Delivered":
            print(f"Delivery Date: {shipment.delivery_date}")
            print(f"Delivery Time: {shipment.delivery_time}")

    def view_all_shipments(self):
        if not self.shipments:
            print("No shipments in the system.")
            return

        headers = ["Shipment ID", "Customer ID", "Origin", "Destination", "Weight (kg)", 
                    "Vehicle ID", "Status", "Delivery Date", "Delivery Time"]
        data = [shipment.to_list() for shipment in self.shipments]

        print("\nAll Shipments:")
        self.display_tabular_records(headers, data)

        print(f"\nTotal shipments: {len(self.shipments)}")

    def get_valid_shipment_id(self):
        while True:
            shipment_id = input("Enter Shipment ID (e.g., S123): ")
            if not re.match(SHIPMENT_ID_FORMAT, shipment_id):
                print("Error: Invalid Shipment ID format. Please use S followed by 3 digits.")
                continue
            if any(shipment.shipment_id == shipment_id for shipment in self.shipments):
                print("Error: Shipment ID already exists. Please enter a unique ID.")
                continue
            return shipment_id

    def get_valid_customer_id(self):
        while True:
            customer_id = input("Enter Customer ID: ")
            if self.customer_management.find_customer(customer_id):
                return customer_id
            print("Error: Customer not found. Please enter a valid Customer ID.")

    def get_valid_weight(self):
        while True:
            try:
                weight = float(input("Enter shipment weight (in kg): "))
                if weight <= 0:
                    print("Error: Weight must be a positive value")
                    continue
                return weight
            except ValueError:
                print("Error: Please enter a valid number for weight.")

    def get_valid_vehicle_id(self):
        available_vehicles = self.fleet_management.get_available_vehicles()
        if not available_vehicles:
            print("Error: No vehicles available for shipment.")
            return None

        
        headers = ["Vechile ID", "Type", "Weight (kg)"]
        data = [vehicles.to_list() for vehicles in available_vehicles]
        print("\nAvailable vehicles:")
        self.display_tabular_records(headers, data)

        while True:
            vehicle_id = input("Enter Vehicle ID for this shipment: ")
            if any(vehicle.vehicle_id == vehicle_id for vehicle in available_vehicles):
                return vehicle_id
            print("Error: Invalid Vehicle ID. Please choose from the available vehicles.")

    def get_customer_shipments(self, customer_id):
        return [shipment for shipment in self.shipments if shipment.customer_id == customer_id]

    def find_shipment(self, shipment_id):
        for shipment in self.shipments:
            if shipment.shipment_id == shipment_id:
                return shipment
        return None


    def menu(self):
        while True:
            print("\n")
            print("-" * 20)
            print("| Shipment Management Menu:")
            print("-" * 20)
            print("1. Create a new shipment")
            print("2. Track a shipment")
            print("3. View all shipments")
            print("4. Quit shipment management")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_shipment()
            elif choice == '2':
                self.track_shipment()
            elif choice == '3':
                self.view_all_shipments()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")


class DeliveryManagement(BaseManagement):
    def __init__(self, shipment_management):
        self.shipment_management = shipment_management

    def mark_shipment_delivery(self):
        # Prompt for Shipment ID
        shipment_id = input("Enter the Shipment ID to mark as delivered: ")

        # Find the shipment
        shipment = self.shipment_management.find_shipment(shipment_id)
        if not shipment:
            print("Error: Shipment not found. Please check the Shipment ID and try again.")
            return

        # Check if the shipment is already delivered
        if shipment.status == 'Delivered':
            print("Error: This shipment has already been marked as delivered.")
            return

        # Get delivery date and time
        delivery_date, delivery_time = self.get_valid_delivery_datetime()
        if not delivery_date or not delivery_time:
            return

        # Update shipment status and delivery information
        shipment.status = "Delivered"
        shipment.delivery_date = delivery_date
        shipment.delivery_time = delivery_time

        # Display success message
        print(f"Shipment {shipment_id} has been successfully marked as delivered.")
        print(f"Delivery Date: {shipment.delivery_date}")
        print(f"Delivery Time: {shipment.delivery_time}")

    def view_delivery_status_shipment(self):
        # Prompt for Shipment ID
        shipment_id = input("Enter the Shipment ID to view delivery status: ")

        # Find the shipment
        shipment = self.shipment_management.find_shipment(shipment_id)
        if not shipment:
            print("Error: Shipment not found. Please check the Shipment ID and try again.")
            return

        # Display shipment status and details
        print(f"\nShipment {shipment_id} Status:")
        print(f"Status: {shipment.status}")
        print(f"Origin: {shipment.origin}")
        print(f"Destination: {shipment.destination}")
        print(f"Weight: {shipment.weight} kg")
        print(f"Vehicle ID: {shipment.vehicle_id}")

        if shipment.status == "Delivered":
            print(f"Delivery Date: {shipment.delivery_date}")
            print(f"Delivery Time: {shipment.delivery_time}")
        else:
            print("This shipment has not been delivered yet.")

    def get_valid_delivery_datetime(self):
        while True:
            date_input = input("Enter delivery date (DD/MM/YYYY): ")
            time_input = input("Enter delivery time (HH:MM): ")

            try:
                # Validate date format
                delivery_date = datetime.strptime(date_input, "%d/%m/%Y").date()

                # Validate time format
                delivery_time = datetime.strptime(time_input, "%H:%M").time()

                # Check if the delivery date and time are not in the future
                current_datetime = datetime.now()
                input_datetime = datetime.combine(delivery_date, delivery_time)

                if input_datetime > current_datetime:
                    print("Error: Delivery date and time cannot be in the future.")
                    continue

                return date_input, time_input
            except ValueError:
                print("Error: Invalid date or time format. Please use DD/MM/YYYY for date and HH:MM for time.")

    def menu(self):
        while True:
            print("\n")
            print("-" * 20)
            print("| Delivery Management Menu:")
            print("-" * 20)
            print("1. Mark Shipment delivery")
            print("2. View delivery status for a shipment")
            print("3. Quit delivery management")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.mark_shipment_delivery()
            elif choice == '2':
                self.view_delivery_status_shipment()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

class MainMenu:
    def __init__(self):
        # Initialize Fleet Management
        self.fleet_manager = FleetManagement()

        # Initialize Shipment Management (needs Fleet Management for vehicle validation)
        self.shipment_manager = ShipmentManagement(self.fleet_manager, None)  # Customer Management will be added later

        # Initialize Customer Management (needs Shipment Management for viewing customer shipments)
        self.customer_manager = CustomerManagement(self.shipment_manager)

        # Update Shipment Management with Customer Management reference
        self.shipment_manager.customer_management = self.customer_manager

        # Initialize Delivery Management (needs Shipment Management for updating shipment status)
        self.delivery_manager = DeliveryManagement(self.shipment_manager)

    def display_menu(self):
        print("\n")
        print("-" * 20)
        print("| Main Menu:")
        print("-" * 20)
        print("1. Fleet Management")
        print("2. Customer Management")
        print("3. Shipment Management")
        print("4. Delivery Management")
        print("0. Quit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.fleet_manager.menu()
            elif choice == '2':
                self.customer_manager.menu()
            elif choice == '3':
                self.shipment_manager.menu()
            elif choice == '4':
                self.delivery_manager.menu()
            elif choice == '0':
                print("Thank you for using the Transportation Logistics System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Create an instance of MainMenu and run the program
main_menu = MainMenu()
main_menu.run()