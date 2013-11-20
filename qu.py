# qu.py
# Alex Claman

from rooms import *

# Room constructor is organized thusly: (north, east, south, west, room_name, room_desc, object_1, object_1_desc, object_2,
# object_2_desc, object_3, object_3_desc, clue)
# Room 1 has North and West entrances
room1 = Room(True, False, False, True, 'Living Room', 'A generic living room', 'couch', 'This is just a couch. Get over it.', 'lamp', 'I love lamp', 'TV', 'Just playing some static', 'May all trouble begone with OxiClean.')
# Room 2 has North and East entrances
room2 = Room(True, True, False, False, 'Dining Room', 'There is a table and a cabinet. The floor is covered by a thick carpet.', 'table', 'A massive oak table.', 'cabinet', 'Contains cutlery, utensils, and plates.', 'carpet', 'An abnormally thick carpet. There might be something under it.', 'Everything is a lie. Except the cake. It is delicious.')
# Room 3 has South and East entrances
room3 = Room(False, True, True, False, 'Parlor', 'There are several armchairs, a coffee table.', 'armchair', 'An exceptionally comfortable leather armchair.', 'coffee tabls', 'Has a few magazines scattered atop its surface.', 'china', 'Not the country, Einstein.', 'Avoid the tea. It is terrible today.')
# Room 4 has South and West elements
room4 = Room(False, False, True, True, 'Bedroom', 'There is a bed and a wardrobe.', 'bed', 'A luxurious four-poster bed with something under it. It is not yours. Step away.', 'wardrobe', 'Contains a large number of old fur coats. May or may not contain a portal to Narnia.', 'something', 'A locked chest.', 'A diary page reading: cruncy peanut butter is better.')

room1.setConnectedRooms(room4)
room1.setConnectedRooms(room2)
room2.setConnectedRooms(room1)
room2.setConnectedRooms(room3)
room3.setConnectedRooms(room2)
room3.setConnectedRooms(room4)
room4.setConnectedRooms(room3)
room4.setConnectedRooms(room1)
room1Con = room1.getConnectedRooms()
room2Con = room2.getConnectedRooms()
room3Con = room3.getConnectedRooms()
room4Con = room4.getConnectedRooms()
print room1Con, room2Con, room3Con, room4Con

startRoom = room1
currentRoom = room1

# def playerMove(move,room):
  # if move in room.getDirections():

# def main():
#   command = raw_input(">")
#   if command == 'north' or command == 'south' or command == 'east' or command == 'west':
#     playerMove(command, currentRoom)

# main()