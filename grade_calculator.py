def grade_calculator():
    # Get name with validation
    while True:
        name = input("Enter Name: ").strip()
        if name and not name.isdigit():  # Check if name is not empty and not just numbers
            break
        else:
            print("Invalid Name! Please enter a valid name.")

    # Get marks with validation
    while True:
        try:
            marks = int(input("Enter Marks (0-100): "))
            if 0 <= marks <= 100:  # Check if marks are between 0 and 100
                break
            else:
                print("Marks must be between 0 and 100! Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Calculate grade
    if marks >= 90:
        grade = 'A'
        message = "Excellent! Outstanding performance! "
    elif marks >= 80:
        grade = 'B'
        message = "Very Good! Keep it up!"
    elif marks >= 70:
        grade = 'C'
        message = "Good work! Keep practicing!"
    elif marks >= 60:
        grade = 'D'
        message = "Satisfactory! Can do better!"
    else:
        grade = 'F'
        message = "Need improvement! Work harder!"

    # Display the result
    print(f"\nRESULTS FOR {name.title()}:")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


# Call the function
grade_calculator()