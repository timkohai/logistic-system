# Logistics Management System

## Description
The Logistics Management System is a comprehensive Python-based application designed to streamline and automate various aspects of logistics operations. This system integrates fleet management, customer management, shipment tracking, and delivery management into a single, user-friendly interface.

## Features
- **Fleet Management**: Add, update, and remove vehicles from the fleet. Track vehicle details including capacity and fuel consumption.
- **Customer Management**: Manage customer information, including adding new customers, updating details, and viewing customer shipments.
- **Shipment Management**: Create and track shipments, assign vehicles, and monitor shipment status.
- **Delivery Management**: Mark shipments as delivered and view delivery statuses.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/logistics-management-system.git
   ```
2. Navigate to the project directory:
   ```
   cd logistics-management-system
   ```
3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the Logistics Management System:
```
python main.py
```

Follow the on-screen prompts to navigate through different management modules.

## Code Structure
- `main.py`: Entry point of the application
- `fleet_management.py`: Contains FleetManagement class and related vehicle classes
- `customer_management.py`: Handles customer-related operations
- `shipment_management.py`: Manages shipment creation and tracking
- `delivery_management.py`: Handles delivery status updates

## Object-Oriented Design
This project demonstrates key OOP principles:
- **Encapsulation**: Data and methods are encapsulated within appropriate classes.
- **Inheritance**: Vehicle types (e.g., Truck, Van) inherit from a base Vehicle class.
- **Polymorphism**: Implemented through method overriding in vehicle classes.

## Contributing
Contributions to the Logistics Management System are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact
For any queries or suggestions, please contact [Your Name] at [your.email@example.com].