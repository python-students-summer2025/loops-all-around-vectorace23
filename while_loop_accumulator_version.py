def get_starting_number():

    

    number_valid = True

    while number_valid:
        amount_of_bottles = input("Enter the amount of bottles that you would like for this program of \"99 bottles\"").strip()

        if amount_of_bottles.isnumeric():
            amount_of_bottles = int(amount_of_bottles)
            if amount_of_bottles >= 1:
                return amount_of_bottles


def sing(number):
    while number > 0:
        if number == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
        else:
            print(f"{number} bottles of beer on the wall, {number} bottles of beer.")
            if number - 1 == 1:
                print("Take one down, pass it around, 1 bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {number - 1} bottles of beer on the wall.\n")
        number -= 1