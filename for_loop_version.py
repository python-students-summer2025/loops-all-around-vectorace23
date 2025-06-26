def get_starting_number():

    number_valid = True

    while number_valid:
        amount_of_bottles = input("Enter the amount of bottles that you would like for this program of \"99 bottles\": ").strip()

        if amount_of_bottles.isnumeric():
            amount_of_bottles = int(amount_of_bottles)
            if amount_of_bottles >= 1:
                number_valid = False
                return amount_of_bottles
                

def sing(num_bottles):
    

    for x in range(num_bottles, 0, -1):
        if x == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
        else:
            print(f"{x} bottles of beer on the wall, {x} bottles of beer.")
            if x - 1 == 1:
                print("Take one down, pass it around, 1 bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {x - 1} bottles of beer on the wall.\n")



