# Vacuum Cleaner Agent

roomA = "Dirty"
roomB = "Dirty"
position = "A"

while roomA == "Dirty" or roomB == "Dirty":

    if position == "A":
        if roomA == "Dirty":
            print("Cleaning Room A")
            roomA = "Clean"

        print("Moving to Room B")
        position = "B"

    else:
        if roomB == "Dirty":
            print("Cleaning Room B")
            roomB = "Clean"

        print("Moving to Room A")
        position = "A"

print("Both rooms are clean")
print("Goal State Reached")