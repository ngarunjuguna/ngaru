import csv
import datetime

# Function to collect car wash service data
def collect_data():
    # Collect customer information
    customer_name = input("Enter customer's name: ")
    car_type = input("Enter car type (e.g., sedan, SUV, truck): ")
    
    # Collect service details
    print("Select the car wash service: ")
    print("1. Basic")
    print("2. Premium")
    print("3. Full-Service")
    
    service_choice = input("Enter the number corresponding to the service: ")

    # Map service choices to service names and prices
    service_dict = {
        '1': ("Basic", 10),
        '2': ("Premium", 20),
        '3': ("Full-Service", 30)
    }
    
    if service_choice not in service_dict:
        print("Invalid choice. Please select a valid service.")
        return
    
    service_name, service_price = service_dict[service_choice]
    
    # Record payment details
    payment_amount = float(input(f"Enter the payment amount for {service_name}: "))
    
    # Get current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Prepare data to be written to CSV
    data_row = [customer_name, car_type, service_name, service_price, payment_amount, timestamp]
    
    # Write data to CSV file
    with open("carwash_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data_row)
    
    print(f"Thank you {customer_name} for using our {service_name} service!")
    print("Your payment has been recorded.")

# Function to display all collected data
def display_data():
    try:
        with open("carwash_data.csv", mode="r") as file:
            reader = csv.reader(file)
            # Print header if file has data
            print("\nCar Wash Data Collection:\n")
            print("Customer Name | Car Type | Service Type | Service Price | Amount Paid | Date & Time")
            print("-------------------------------------------------------------------------------")
            
            # Loop through each row and print it
            for row in reader:
                print(f"{row[0]:<15} | {row[1]:<8} | {row[2]:<12} | {row[3]:<13} | {row[4]:<10} | {row[5]}")
    except FileNotFoundError:
        print("No data available. The data file does not exist yet.")
    except Exception as e:
        print(f"Error reading the data file: {e}")

# Main function to run the car wash data collection and display
def main():
    while True:
        print("\nCar Wash Data Collection")
        print("-------------------------")
        
        # Ask if the user wants to add data or display existing data
        action_choice = input("Do you want to (1) Add Data or (2) Display Data? Enter 1 or 2: ")
        
        if action_choice == '1':
            collect_data()
        elif action_choice == '2':
            display_data()
        else:
            print("Invalid choice. Please select 1 to add data or 2 to display data.")
        
        continue_choice = input("\nWould you like to perform another action? (y/n): ").lower()
        if continue_choice != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
