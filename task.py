print(r'''

                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure... ")
print("...Can you face the dangers on the island?")
points = 0
input("Type 'Y' to continue, 'N' to leave\n")
direction_path = input('''You have found yourself at a cross roads...
Type 'R' to take the right path and 'L' to take the left path\n''')
if direction_path =="L":
    swimming_or_waiting = input('''You made your way along the path and ended up in front of a lake...
Type 'S' to swim across the lake or type 'W' to wait and look around for any clues.\n''')
    if swimming_or_waiting == "W":
        door_colours = input('''You avoided the lake and ended up in front of three doors -blue, yellow and red- choose wisely or you will be stuck in the island forever... 
Type 'B' for the blue door, 'Y' for the yellow door and 'R' for the red door.\n''')
        if door_colours == "B":
            print("You entered a room full of fire... GAME OVER.")
        elif door_colours == "Y":
            print("You entered a room filled with gold and diamonds... You win!")
        elif door_colours == "R":
            print("You entered room full of hungry cannibals... GAME OVER.")
        else:
            print("You typed in the wrong input... GAME OVER.")
    else:
        print("You got attacked by a hungry alligator... GAME OVER.")
else:
    print("You ended up in a jungle and got mauled by a bear... GAME OVER.")