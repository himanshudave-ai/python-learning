while True:
    try:
        marks = float(input("Enter student marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100!")
        else:
            print("Valid Marks:", marks)
            break

    except ValueError:
        print("Invalid input! Enter numeric marks.")