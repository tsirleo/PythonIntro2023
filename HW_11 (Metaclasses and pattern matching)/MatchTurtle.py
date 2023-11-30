x, y = 0, 0
last_move = ""

while data := input():
    match data.split(" ", 1):
        case ["say", msg]:
            print(msg)
        case ["info", param]:
            match param:
                case "x":
                    print(x)
                case "y":
                    print(y)
                case "xy":
                    print(f"{x} {y}")
        case ["move", direction]:
            match direction:
                case "s":
                    y -= 1
                    last_move = direction
                case "n":
                    y += 1
                    last_move = direction
                case "w":
                    x -= 1
                    last_move = direction
                case "e":
                    x += 1
                    last_move = direction
                case _:
                    print(f"Cannot move to {direction}")
        case ["move"]:
            match last_move:
                case "s":
                    y -= 1
                case "n":
                    y += 1
                case "w":
                    x -= 1
                case "e":
                    x += 1
        case ["retreat"]:
            match last_move:
                case "s":
                    y += 1
                case "n":
                    y -= 1
                case "w":
                    x += 1
                case "e":
                    x -= 1

print(f"{x} {y}")
