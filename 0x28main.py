def validate_age():
    try:
        age = int(input("Enter your age: "))
        if age < 18:
            raise ValueError("Age must be at least 18.")

    except ValueError as e:
        print(f"Error: {e}")

    else:
        print("Access granted")

validate_age()