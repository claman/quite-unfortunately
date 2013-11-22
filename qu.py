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
# Room 1 has North and West entrances
room1 = Room('Living Room', 'A generic living room containing a couch,\
  a lit lamp, and a TV.',
  'couch', 'This is just a couch with a remote on it. Get over it.',
  'lamp', 'It is casting a strange shadow on the wall.', 'TV',
  'Just playing some static.',
  'An infomercial: May all trouble begone with OxiClean.', 'use remote')
# Room 2 has North and East entrances
room2 = Room('Dining Room', 'There is a table and a cabinet.\
  The floor is covered by a thick carpet', 'table', 'A massive\
  oak table.', 'cabinet','Contains cutlery, utensils, and plates.', 'carpet',
  'An abnormally thick carpet. There might be something under it.', 'You\
  find a old, yellowed letter with a key inside. It reads: Everything\
  is a lie. Except the cake. It is delicious.', 'lift carpet')
# Room 3 has South and East entrances
room3 = Room('Parlor', 'There are several armchairs and a coffee table.',
  'armchair', 'An exceptionally comfortable leather armchair.',
  'coffee table', 'Has some coffee cups and a few magazines scattered\
  atop its surface.', 'coffee cups', 'Sadly, they do not contain coffee.',
  'The headline reads: Avoid the tea. It\'s terrible today.', 'read magazine')
# Room 4 has South and West elements
room4 = Room('Bedroom', 'There is a bed and a wardrobe.','bed',
  'A luxurious four-poster bed with something under it. It is not yours.\
  Step away.', 'wardrobe', 'Contains a large number of old fur coats.\
  May or may not contain a portal to Narnia.', 'something',
  'A locked chest.', 'The chest contains a diary page reading only:\
  crunchy peanut butter is better.', 'unlock chest')

# This next block sets the connections between rooms
room1.setConnectedRoom(room4,'north')
room1.setConnectedRoom(room2,'west')
room2.setConnectedRoom(room1,'east')
room2.setConnectedRoom(room3,'north')
room3.setConnectedRoom(room2,'south')
room3.setConnectedRoom(room4,'east')
room4.setConnectedRoom(room3,'west')
room4.setConnectedRoom(room1,'south')

room2.setItem('key')

def changeRoom(room):
  current_room = room

def playerMove(move,current_room):
  if move in current_room.getExits():
    connected_rooms = current_room.getConnectedRooms()
    if move == 'north':
      newRoom = current_room.north_room
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

def addToBackpack(item):
  backpack.append(item)

def exitGame():
  sys.exit('Exiting Game...')

# if 'key' in backpack:
#   unlock_chest
# else:
#   'the chest is locked'

def main():
  current_room = room1
  backpack = []
  print 'Move using north, south, east, and west. Explore. Investigate. Escape.'
  while True:
    command = raw_input(">")
    if command in ('north', 'south', 'east', 'west'):
      current_room = playerMove(command,current_room)
      info = current_room.getRoomInfo()
      print info
    elif command == 'look':
      info = current_room.getRoomInfo()
      print info
    elif len(command) > 8 and command[0:7] == 'examine':
      entries = command.split(' ')
      atwas = entries[1]
      if atwas in current_room.listObjects():
        object_info = current_room.getObjectDescription(atwas)
        print object_info
      else:
        print 'I don\'t know what that is.'
    elif command[0:2] == 'get':
      entries = command.split(' ')
      item = entries[1]
      if item == current_room.item:
        addToBackpack(item)
        item,'was added to your backpack.'
      else:
        print 'I can\'t do that.'
    elif command == 'backpack':
      if backpack != []:
        print backpack
      else:
        print 'Your backpack is empty.'
    elif command == current_room.getClueAction():
      print current_room.clue
    elif command in ('exit','quit','q'):
      exitGame()
    else:
      print 'I don\'t know what that means.'
main()