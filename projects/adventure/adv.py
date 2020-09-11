from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#Vars

stack = []
visited = set()

while len(world.rooms) > len(visited):

    tempPath = [] #temp path variable
    options = player.current_room.get_exits() #returns directions you can go

    for option in options: #loop through potential directions you could go and if one isn't already in 'visited' go there
        if player.current_room.get_room_in_direction(option) not in visited:
            tempPath.append(option)

    visited.add(player.current_room)

    if len(tempPath) != 0:
        stack.append(tempPath[len(tempPath) - 1])
        player.travel(tempPath[len(tempPath) - 1])
        traversal_path.append(tempPath[len(tempPath) - 1])

    else: #if reaches a dead end...

        end = stack.pop()

        returnDir = None

        if end == "n":
            returnDir = "s"
        elif end == "s":
            returnDir = "n"
        elif end == "e":
            returnDir = "w"
        elif end == "w":
            returnDir = "e"

        player.travel(returnDir)
        traversal_path.append(returnDir)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")