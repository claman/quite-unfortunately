# qu.py
# Alex Claman

# room3 -- room4
#   |        |
#   |        |
# room2 -- room1

from rooms import *
import sys

# Room constructor is organized thusly: (room_name, room_desc, object_1,
# object_1_desc, object_2, object_2_desc, object_3, object_3_desc, clue)
room1 = Room('Living Room', 'A generic living room containing a couch,\
  a lit lamp, and a TV.',
  'couch', 'This is just a couch with a remote on it. Get over it.',
  'lamp', 'It is casting a strange shadow on the wall.', 'TV',
  'Just playing some static.',
  'An infomercial: May all trouble begone with OxiClean.', 'use remote')
room2 = Room('Dining Room', 'There is a table and a cabinet.\
  The floor is covered by a thick carpet', 'table', 'A massive\
  oak table.', 'cabinet','Contains cutlery, utensils, and plates.', 'carpet',
  'An abnormally thick carpet. There might be something under it.', 'You\
  find a old, yellowed letter with a key inside. It reads: Everything\
  is a lie. Except the cake. It is delicious.', 'lift carpet')
room3 = Room('Parlor', 'There are several armchairs and a coffee table.',
  'armchair', 'An exceptionally comfortable leather armchair.',
  'coffee table', 'Has some coffee cups and a few magazines scattered\
  atop its surface.', 'coffee cups', 'Sadly, they do not contain coffee.',
  'The headline reads: Avoid the tea. It\'s terrible today.', 'read magazine')
room4 = Room('Bedroom', 'There is a bed and a wardrobe.','bed',
  'A luxurious four-poster bed with something under it. It is not yours.\
  Step away.', 'wardrobe', 'Contains a large number of old fur coats.\
  May or may not contain a portal to Narnia.', 'something',
  'A locked chest.', 'The chest contains a diary page reading only:\
  crunchy peanut butter is better.', 'unlock chest')
room5 = ()
room6 = ()
room7 = ()
room8 = ()
room9 = ()
room10 = ()
room11 = ()
room12 = ()
room13 = ()
room14 = ()
room15 = ()
room16 = ()

# This next block sets the connections between rooms
room1.setConnectedRoom(room4,'north') # room4 is north of room1
room1.setConnectedRoom(room2,'west')  # room2 is west of room1
room2.setConnectedRoom(room1,'east')  # room1 is east of room2
room2.setConnectedRoom(room3,'north') # room3 is north of room2
room3.setConnectedRoom(room2,'south') # room2 is south of room3
room3.setConnectedRoom(room4,'east')  # room4 is east of room3
room4.setConnectedRoom(room3,'west')  # room3 is west of room4
room4.setConnectedRoom(room1,'south') # room1 is south of room4

room2.setItem('key')

def playerMove(move,current_room):
  if move in current_room.getExits():   # checks if the move direction is valid
    if move == 'north':                 # move north, set current_room to
      newRoom = current_room.north_room # the room north of current_room
      return newRoom
    elif move == 'south':
      newRoom = current_room.south_room
      return newRoom
    elif move == 'east':
      newRoom = current_room.east_room
      return newRoom
    elif move == 'west':
      newRoom = current_room.west_room
      return newRoom
  else:
    print 'You can\'t move in that direction.'

def exitGame():
  sys.exit('Exiting Game...')

# if 'key' in backpack:
#   unlock_chest
# else:
#   'the chest is locked'

def main():
  current_room = room1
  backpack = []
  print 'Move using north, south, east, and west. Explore. Escape.'
  while True:
    command = raw_input(">")
    words = command.split()
    if words[0] in ('north', 'south', 'east', 'west'):
      current_room = playerMove(command,current_room)
      info = current_room.getRoomInfo()
      print info
    elif words[0] == 'look':
      info = current_room.getRoomInfo()
      print info
    elif words[0] == 'get':
      if words[1] == current_room.item:
        backpack.append(words[1])
        print words[1],'was added to your backpack.'
      else:
        print 'I can\'t do that.'
    elif words[0] == 'examine':
      if words[1] in current_room.listObjects():
        object_info = current_room.getObjectDescription(words[0])
        print object_info
      else:
        print 'I don\'t know what that is.'
    elif words[0] == 'backpack':
      if backpack != []:
        print backpack
      else:
        print 'Your backpack is empty.'
    elif command == current_room.getClueAction():
      print current_room.clue
    elif words[0] in ('exit','quit','q'):
      exitGame()
    else:
      print 'I don\'t know what that means.'
main()