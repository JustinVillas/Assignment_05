# Create program  that ask three numbers.
# Find the lowest number using only if-else statement.
# Display the lowest number

def numbers():
    numberA = int(input("number a : "))
    numberB = int(input("number b : "))
    numberC = int(input("number c : "))
    return numberA,  numberB,  numberC


# Ask for three numbers.
numberA,  numberB,  numberC = numbers()

# Get the lowest number.
if numberA < numberB and numberA < numberC:
    print(f"The lowest number is {numberA}. ")
else:
    if numberB < numberA and numberB < numberC:
        print(f"The lowest number is {numberB}. ")
    else:
        if numberC < numberB and numberC < numberA:
            print(f"The lowest number is {numberC}. ")
        else:
            if numberB < numberC and numberB < numberA:
                Print(f"The lowest number is {numberC}. ")
