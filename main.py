def get_customer_details():
    """Ask the user for customer name, ID, and units consumed."""
    customer_name = input("Enter customer name: ")
    customer_id = input("Enter customer ID: ")

    units_consumed = float(input("Enter electricity units consumed: "))

    while units_consumed < 0:
        print("Units consumed cannot be negative. Please enter a valid number.")
        units_consumed = float(input("Enter electricity units consumed: "))

    return customer_name, customer_id, units_consumed


def calculate_bill(units):
    """Calculate energy charge using the given slabs and add a fixed service charge."""
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = (100 * 2) + ((units - 100) * 4)
    elif units <= 500:
        energy_charge = (100 * 2) + (100 * 4) + ((units - 200) * 6)
    else:
        energy_charge = (100 * 2) + (100 * 4) + (300 * 6) + ((units - 500) * 8)

    service_charge = 100
    final_bill = energy_charge + service_charge
    return energy_charge, service_charge, final_bill


def display_bill(name, customer_id, units, energy_charge, service_charge, final_bill):
    """Display the final electricity bill in a clean format."""
    print("\n====================================")
    print("         Smart Electricity Bill")
    print("====================================")
    print(f"Customer Name     : {name}")
    print(f"Customer ID       : {customer_id}")
    print(f"Units Consumed    : {units:.2f}")
    print(f"Energy Charge     : Rs. {energy_charge:.2f}")
    print(f"Service Charge    : Rs. {service_charge:.2f}")
    print(f"Final Bill Amount : Rs. {final_bill:.2f}")
    print("====================================\n")


def main():
    """Main program flow."""
    customer_name, customer_id, units = get_customer_details()
    energy_charge, service_charge, final_bill = calculate_bill(units)
    display_bill(customer_name, customer_id, units, energy_charge, service_charge, final_bill)


if __name__ == "__main__":
    main()