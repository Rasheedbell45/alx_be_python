FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature (e.g., 100F or 37C): ").strip().upper()

        # Extract the numeric value and unit
        if temp_input.endswith("F"):
            temp_value = float(temp_input[:-1])
            result = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {result:.2f}°C")
        elif temp_input.endswith("C"):
            temp_value = float(temp_input[:-1])
            result = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {result:.2f}°F")
        else:
            raise ValueError("Invalid unit. Please end your input with 'C' or 'F'.")

    except ValueError as ve:
        print("Invalid temperature. Please enter a numeric value.")
        print(f"Details: {ve}")

if __name__ == "__main__":
    main()
