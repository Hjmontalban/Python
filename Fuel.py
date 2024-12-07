# Define the car types with their corresponding fuel efficiency, weight, and passenger capacity
car_types = {
    1: {'name': 'sedan', 'fuel_efficiency': 15, 'weight': 1500, 'passenger_capacity': 5},
    2: {'name': 'suv', 'fuel_efficiency': 8, 'weight': 2000, 'passenger_capacity': 7},
    3: {'name': 'truck', 'fuel_efficiency': 20, 'weight': 3000, 'passenger_capacity': 2},
}

# Define the fuel types with their corresponding price
fuel_types = {
    1: {'name': 'gasoline', 'price': 58.50},
    2: {'name': 'diesel', 'price': 51.00}
}

# Define the road conditions with a factor that impacts fuel efficiency
road_conditions = {
    1: {'name': 'normal', 'factor': 1.0},
    2: {'name': 'uphill', 'factor': 1.25},
    3: {'name': 'rough', 'factor': 1.15}
}


# Function to adjust fuel efficiency based on car weight, number of passengers, and road conditions
def adjust_fuel_efficiency(base_efficiency, car_weight, passengers, road_factor):
    # Adjust fuel efficiency based on weight and passenger factors
    weight_factor = 1 + (car_weight - 1500) / 10000
    passenger_factor = 1 + (passengers / 10)

    # Return the adjusted fuel efficiency
    return base_efficiency / (weight_factor * passenger_factor * road_factor)


# Function to calculate fuel consumption and cost
def calculate_fuel_consumption(car_type, fuel_type, distance_km, passengers, road_type):
    # Get car details from the selected car type
    car_info = car_types[car_type]
    base_efficiency = car_info['fuel_efficiency']
    car_weight = car_info['weight']

    # Get road factor based on road condition
    road_factor = road_conditions[road_type]['factor']

    # Adjust the fuel efficiency
    adjusted_efficiency = adjust_fuel_efficiency(base_efficiency, car_weight, passengers, road_factor)

    # Calculate fuel needed and total fuel cost
    fuel_needed = distance_km / adjusted_efficiency
    fuel_cost = fuel_needed * fuel_types[fuel_type]['price']

    return fuel_needed, fuel_cost


# Function to predict future travel fuel consumption and costs
def predict_future_travel(car_type, fuel_type, current_distance, future_distance, passengers, road_type):
    # Calculate current and future fuel consumption and cost
    current_fuel_needed, current_fuel_cost = calculate_fuel_consumption(car_type, fuel_type, current_distance,
                                                                        passengers, road_type)
    future_fuel_needed, future_fuel_cost = calculate_fuel_consumption(car_type, fuel_type, future_distance, passengers,
                                                                      road_type)

    # Calculate total distance, fuel needed, and cost
    total_distance = current_distance + future_distance
    total_fuel_needed = current_fuel_needed + future_fuel_needed
    total_fuel_cost = current_fuel_cost + future_fuel_cost

    return {
        'total_distance': total_distance,
        'current_fuel_needed': current_fuel_needed,
        'future_fuel_needed': future_fuel_needed,
        'total_fuel_needed': total_fuel_needed,
        'current_fuel_cost_php': current_fuel_cost,
        'future_fuel_cost_php': future_fuel_cost,
        'total_fuel_cost_php': total_fuel_cost
    }


# Prompt the user to select car type
print("Car types: \n1. Sedan\n2. SUV\n3. Truck")
car_type = int(input("Select car type (1-3): "))
if car_type not in car_types:
    print("Invalid car type selected. Program will terminate.")
    exit()

# Prompt the user to select fuel type
print("\nFuel types: \n1. Gasoline\n2. Diesel")
fuel_type = int(input("Select fuel type (1-2): "))
if fuel_type not in fuel_types:
    print("Invalid fuel type selected. Program will terminate.")
    exit()

# Prompt for travel distances and number of passengers
current_distance = float(input("\nEnter current travel distance (in km): "))
future_distance = float(input("Enter future travel distance to predict (in km): "))
passengers = int(input("Enter the number of passengers: "))

# Check if the number of passengers exceeds 8
if passengers >= 8:
    print("Number of passengers exceeds capacity. Program will terminate.")
    exit()

# Prompt the user to select road type
print("\nRoad types: \n1. Normal\n2. Uphill\n3. Rough")
road_type = int(input("Select road type (1-3): "))
if road_type not in road_conditions:
    print("Invalid road type selected. Program will terminate.")
    exit()

# Calculate and display the result for current and future travel
result = predict_future_travel(car_type, fuel_type, current_distance, future_distance, passengers, road_type)

# Display results
print(f"\nFor a {car_types[car_type]['name'].capitalize()} running on {fuel_types[fuel_type]['name'].capitalize()}:")
print(f"Current distance traveled: {current_distance} km")
print(f"Fuel needed for current distance: {result['current_fuel_needed']:.2f} liters")
print(f"Fuel cost for current distance: PHP {result['current_fuel_cost_php']:.2f}\n")

print(f"Predicted future distance: {future_distance} km")
print(f"Fuel needed for future distance: {result['future_fuel_needed']:.2f} liters")
print(f"Fuel cost for future distance: PHP {result['future_fuel_cost_php']:.2f}\n")

print(f"Total distance to travel: {result['total_distance']} km")
print(f"Total fuel needed: {result['total_fuel_needed']:.2f} liters")
print(f"Total fuel cost: PHP {result['total_fuel_cost_php']:.2f}")

import time

# Start measuring the time using a high-resolution timer
start = time.perf_counter()

# Simulate some process (e.g., sleep for 2 seconds)
time.sleep(2)

# Stop measuring the time
stop = time.perf_counter()

# Calculate the duration in microseconds
duration_microseconds = (stop - start) * 1_000_000

# Display the execution time in microseconds
print(f"Execution time: {duration_microseconds:.0f} microseconds")
