
rooms = {"A": "Dirty", "B": "Dirty"}
position = "A"

while True:
    print("Vacuum cleaner is in room", position)

    if rooms[position] == "Dirty":
        rooms[position] = "Clean"
        print("Room", position, "cleaned")

    if position == "A":
        position = "B"
    else:
        break

print("Final status:", rooms)
