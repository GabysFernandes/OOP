"""from magic import get_eight_ball_response
question = input("Ask the magic eight ball a question: ")

try:
    if not question.strip():
        raise ValueError("question can not be empty")
    answer = get_eight_ball_response()
    print(f"\n Magic Eight ball Says: {answer}")
except ValueError as error:
    print(f"\n Input Error: {error}")"""



""" //////////////////////////////////////////////////////////////"""  

"""

balance = 500.00
print(f"\n Welcome to the class Bank")

while True:
    print(f"\n 1. Check balance")
    print(" 2. Deposit Money")
    print(" 3. Withdraw Money")
    print(" 4. Exit")

    option = input("Choose an option: ")
    match option:
        case "1":
            print(f"Your balance is:  {balance:.2f}")
        case "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    raise ValueError("Amount most be greater than zero.")
                balance += amount
                print(f"Deposit successful!")
                print(f"New balance is:  {balance:.2f}")
            except ValueError as error:
                print("Error:",error)

        case "3":
            try:
                amount = float(input("Enter withdraw: "))
                if amount <= 0:
                    raise ValueError("Amount most be greater than zero.")
                balance -= amount
                print(f"Withdraw successful!")
                print(f"New balance is: {balance:.2f}")
            except ValueError as error:
                print("Error:",error)

        case "4":
            print("Thank you for using Class Bank!")
            break
"""


"""///////////////////////////////////////////////////////////////////////////////"""

print(f"\n Temperature Converter")
while True:
    print(" 1. Celsius to Fahrenheits")
    print(" 2. Fahrenheits to Celsius")
    print(" 3. Celsius to Kelvin")

    option = input("Choose an option: ")

    try:
        temperature = float(input("Enter the temperature: "))

        match option:
            case "1":
                result = (temperature *9/5) + 32
                print(f"{temperature} C = {result:.2f} -F")
            case "2":
                result2 = (temperature - 32) / 1.8
                print(f"{temperature} F = {result2:.2f} -C")
            case "3":
                result3 = temperature + 273.15
                print(f"{temperature} C = {result3:.2f} -K")
                break
            
    except ValueError:
        print("Please enter a valid number.")

