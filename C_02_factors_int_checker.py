# enter a number that is more than zero
def num_check(question):
    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:


        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = float(input(question))

            # check that number is between 1 and 200
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine Goes Here
while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break


for item in range(0,2):
    width = num_check("Width: ")
    print(width)

print()

for item in range(0,2):
    height = num_check("Height: ")
    print(height)

print()