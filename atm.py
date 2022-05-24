welcome = input("Welcome to ABC ATM Machine. ")

my_balance = 100

pin_number = 1234
num_of_tries = 3

while num_of_tries > 0:
    try:
        my_pin = int(input("Please enter your four digit PIN number in a number format: " ))
    except ValueError:
        print("PIN number must only be in integers. Try Again")
        continue

    if my_pin == pin_number:
        print(f"Your balance is {my_balance}. Goodbye")
        break

    if my_pin != pin_number:
        print("Invalid PIN.")
        num_of_tries -= 1

    if num_of_tries == 0:
        print("After three tries, your bank account is locked!!!!! The police is on its way!!!!")
        break
