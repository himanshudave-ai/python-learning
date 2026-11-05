try:
    numbers = [10, 20, 30]

    index = int(input("Enter index (0-2): "))

    result = numbers[index]

    print("Value:", result)

except ValueError:
    print("Error: Please enter an integer!")

except IndexError:
    print("Error: Index is out of range!")

except Exception as e:
    print("Unexpected Error:", e)