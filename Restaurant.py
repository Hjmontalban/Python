import random
import time


class Restaurant:
    def __init__(self, name, cost_per_order):
        self.name = name
        self.cost_per_order = cost_per_order
        self.total_sales = 0
        self.sales_data = []

    def display_menu(self):
        print("\n----- Menu -----")
        for idx, (item, price) in enumerate(menu.items(), start=1):
            print(f"{idx}. {item}: ₱{price:.2f}")
        print("----------------")

    def random_customize_order(self):
        extra_cost = 0
        size_options = {1: "Regular", 2: "Medium", 3: "Large"}
        size_choice = random.choice(list(size_options.keys()))  # Randomly select a size
        size = size_options[size_choice]

        if random.choice([True, False]):
            extra_cost += 5.00  # Extra cheese
        if random.choice([True, False]):
            extra_cost += 10.00  # Extra toppings
        return extra_cost, size

    def manual_customize_order(self):
        extra_cost = 0
        size_options = {1: "Regular", 2: "Medium", 3: "Large"}
        print("Choose size:")
        for number, size in size_options.items():
            print(f"{number}. {size}")

        while True:
            try:
                size_choice = int(input("Enter the size number: "))
                if size_choice in size_options:
                    size = size_options[size_choice]
                    break
                else:
                    print("Invalid choice. Please select a valid size number.")
            except ValueError:
                print("Please enter a valid number.")

        add_cheese = input("Add extra cheese? (Y/N): ").strip().upper()
        add_toppings = input("Add extra toppings? (Y/N): ").strip().upper()

        if add_cheese == 'Y':
            extra_cost += 5.00
        if add_toppings == 'Y':
            extra_cost += 10.00

        return extra_cost, size

    def apply_promotions(self, total_orders):
        if total_orders > 1000:
            discount = total_orders * 0.10
            print(f"Applying 10% discount of ₱{discount:.2f} for orders over ₱1000.")
            total_orders -= discount
        return total_orders

    def take_order(self, num_people):
        self.display_menu()
        total_orders = 0
        order_summary = []

        if num_people > 10:
            print("\n*** Number of people exceeds 10, randomizing orders for all. ***")
            random_order_start_time = time.time()  # Start timer for random orders

            for i in range(num_people):
                person_orders = []
                total_person_cost = 0  # Track total cost for the person
                num_items = random.randint(1, 3)  # Randomly choose 1 to 3 items for each person

                for j in range(num_items):
                    order_item = random.choice(list(menu.keys()))
                    order_amount = menu[order_item]
                    extra_cost, size = self.random_customize_order()

                    total_item_cost = order_amount + extra_cost
                    total_orders += total_item_cost
                    total_person_cost += total_item_cost  # Add to person's total
                    person_orders.append(f"{order_item} ({size}, Extra: ₱{extra_cost:.2f}) - ₱{total_item_cost:.2f}")
                    self.sales_data.append(order_item)

                order_summary.append(f"\nPerson {i + 1} ordered:")
                order_summary.extend(person_orders)
                order_summary.append(f"Total for Person {i + 1}: ₱{total_person_cost:.2f}")  # Add total for the person

            random_order_end_time = time.time()  # End timer for random orders
            print(f"\nRandom order generation time: {random_order_end_time - random_order_start_time:.2f} seconds")

        else:
            for i in range(num_people):
                person_orders = []
                total_person_cost = 0  # Track total cost for the person
                num_items = int(input(f"\nHow many items will Person {i + 1} order? "))

                for j in range(num_items):
                    while True:
                        try:
                            choice = int(input(f"Choose item number for Person {i + 1}: "))  # User selects by number
                            if 1 <= choice <= len(menu):
                                order_item = list(menu.keys())[choice - 1]  # Get the item from the menu by index
                                order_amount = menu[order_item]
                                extra_cost, size = self.manual_customize_order()
                                break
                            else:
                                print("Invalid choice. Please select a valid item number.")
                        except ValueError:
                            print("Please enter a valid number.")

                    total_item_cost = order_amount + extra_cost
                    total_orders += total_item_cost
                    total_person_cost += total_item_cost  # Add to person's total
                    person_orders.append(f"{order_item} ({size}, Extra: ₱{extra_cost:.2f}) - ₱{total_item_cost:.2f}")
                    self.sales_data.append(order_item)

                order_summary.append(f"\nPerson {i + 1} ordered:")
                order_summary.extend(person_orders)
                order_summary.append(f"Total for Person {i + 1}: ₱{total_person_cost:.2f}")  # Add total for the person

        self.total_sales += total_orders
        total_orders = self.apply_promotions(total_orders)  # Apply promotions before finalizing total
        print(f"\nTotal for all orders in this round: ₱{total_orders:.2f}")
        print("\n----- Order Summary -----")
        for detail in order_summary:
            print(detail)
        print("--------------------------")

    def check_profitability(self):
        profit = self.total_sales - (self.cost_per_order * len(self.sales_data))
        print(f"\nTotal Profit/Loss: ₱{profit:.2f}")

    def run(self):
        print("\n***** Welcome to The Python Restaurant *****")
        while True:
            while True:
                try:
                    num_people = int(input("Enter the number of people ordering (up to 100,000): "))
                    if 1 <= num_people <= 100000:
                        break
                    else:
                        print("Please enter a number between 1 and 100,000.")
                except ValueError:
                    print("Please enter a valid number.")

            self.take_order(num_people)
            self.check_profitability()
            if input("\nWould you like to place more orders? (Y/N): ").strip().upper() != 'Y':
                print("\nThank you for dining at The Python Restaurant!")
                break


def main():
    global menu
    menu = {"Pasta": 5.99, "Burger": 2.99, "Salad": 1.99, "Pizza": 10.99, "Soda": 1.50, "Coffee": 2.50}
    menu = {item: round(price * 55, 2) for item, price in menu.items()}  # Convert prices to PHP

    restaurant_name = "The Python Restaurant"
    cost_per_order = float(input("Enter the cost incurred by the restaurant per order (in PHP): "))
    restaurant = Restaurant(restaurant_name, cost_per_order)

    start_time = time.time()  # Start timer for total execution
    restaurant.run()
    end_time = time.time()  # End timer for total execution

    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
