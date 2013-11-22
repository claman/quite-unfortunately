# qu.py
# Alex Claman

from rooms import *
import sys

# Room constructor is organized thusly: (room_name, room_desc, object_1,
# object_1_desc, object_2, object_2_desc, object_3, object_3_desc, clue)
room1 = Room('Living Room', 'A generic living room containing a couch,\
  a lit lamp, and a TV.',
  'couch', 'This is just a couch with a remote on it. Get over it.',
  'lamp', 'It is casting a strange shadow on the wall.', 'TV',
  'Just playing some static.',
  'An infomercial blares: Injured? Insane? We can\'t really help. Sorry.',
  'use remote')
  # Letter = I
room2 = Room('Dining Room', 'There is a table and a cabinet.\
  The floor is covered by a thick carpet', 'table', 'A massive\
  oak table.', 'cabinet','Contains cutlery, utensils, and plates.', 'carpet',
  'An abnormally thick carpet. There might be something under it.', 'You\
  find a old, yellowed letter with a key inside. It reads: Everything\
  is a lie. Except the cake. It is exquisite.', 'lift carpet')
room3 = Room('Parlor', 'There are several armchairs and a coffee table.',
  'armchair', 'An exceptionally comfortable leather armchair.',
  'coffee table', 'Has some mugs and a few magazines scattered\
  atop its surface.', 'mugs', 'Sadly, they do not contain coffee.',
  'The headline reads: Avoid the tea. It\'s terrible today.', 'read magazine')
  # Letter = T
room4 = Room('Bedroom', 'There is a bed and a wardrobe.','bed',
  'A luxurious four-poster bed with something under it. It is not yours.\
  Step away.', 'wardrobe', 'Contains a large number of old fur coats.\
  May or may not contain a portal to Narnia.', 'something',
  'A locked chest.', 'The chest contains a page reading only:\
  Bifur, Bofur, and Bombur are dwarves.',
  'unlock chest')
  # Letter = B
room5 = Room('Entry Hall','A large entry hall. Kind of dark and gloomy. \
  There\'s a coatrack, a tapestry hanging on a wall, and a chandelier.',
  'coatrack','It\'s very dusty in that corner. You cough a bit.','tapestry',
  'A very old tapestry depicting the hunt of a unicorn. It\'s probably \
  valuable.', 'chandelier','Strangely, it contains some smoking candles.',
  'You rip the tapestry down from the wall, revealing a message:\
  Do not open the oblong package. It\'s only oil.', 'steal tapestry')
  # Letter = O
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

# winning: player has to find the recurring letter in each of the
# clues, then find the correct anagram of those letters; additionally
# player must have all items in their backpack
# The word is discombobulating

# This next block sets the connections between rooms
room1.setConnectedRoom(room4,'north') # room4 is north of room1
room1.setConnectedRoom(room2,'west')  # room2 is west of room1
room2.setConnectedRoom(room1,'east')  # room1 is east of room2
room2.setConnectedRoom(room3,'north') # room3 is north of room2
room3.setConnectedRoom(room2,'south') # room2 is south of room3
room3.setConnectedRoom(room4,'east')  # room4 is east of room3
room4.setConnectedRoom(room3,'west')  # room3 is west of room4
room4.setConnectedRoom(room1,'south') # room1 is south of room4

# room3 -- room4
#   |        |
#   |        |
# room2 -- room1

room2.setItem('key') # changes the item in room2 from None to 'key'
room4.setRequiredItem('key') # changes required_item in room4 to 'key'

def playerMove(move,current_room):
  if move in current_room.getExits():    # check if the move direction is valid
    if move == 'north':                  # if move = north, set new_room to
      new_room = current_room.north_room # the room north of current_room
      return new_room
    elif move == 'south':
      new_room = current_room.south_room
      return new_room
    elif move == 'east':
      new_room = current_room.east_room
      return new_room
    elif move == 'west':
      new_room = current_room.west_room
      return new_room
  else:
    print 'You can\'t move in that direction.'

def exitGame(): # being able to quit the game is a good idea
  sys.exit('Exiting Game...')

def main():
  current_room = room1
  backpack = [] # initialize backpack
  journal = []  # initialize journal
  print 'You have a journal and a backpack.'
  print 'Move using n(orth), s(outh), e(ast), and w(est).'
  print 'Interact with the environment using l(ook), ex(amine), and get.'
  print 'Explore. Investigate. Escape. And remember to check your journal.'
  while True:
    command = raw_input(">")
    words = command.split()
    if words[0] in ('north','south','east','west','n','s','e','w'):
      current_room = playerMove(command,current_room)
      info = current_room.getRoomInfo()
      print info
    elif words[0] in ('look','l'):
      info = current_room.getRoomInfo()
      print info
    elif words[0] == 'get':
      if words[1] == current_room.item:
        backpack.append(words[1])
        print words[1],'was added to your backpack.'
      else:
        print 'I can\'t do that.'
    elif words[0] in ('examine','ex'):
      if words[1] in current_room.listObjects():
        object_info = current_room.getObjectDescription(words[1])
        print object_info
      else:
        print 'I don\'t know what that is.'
    elif words[0] == 'backpack':
      if backpack != []:
        print backpack
      else:
        print 'Your backpack is empty.'
    elif command==current_room.getClueAction() and current_room.solved==False:
      if current_room.required_item in backpack:
        journal.append(current_room.clue)
        print current_room.clue
        current_room.solve()
      elif current_room.required_item == None:
        print current_room.clue
        journal.append(current_room.clue)
        current_room.solve()
      else:
        print 'I\'m sorry. I don\'t know what that means.'
    elif command==current_room.getClueAction() and current_room.solved==True:
      print 'You\'ve already found this clue.'
    elif command == 'read journal':
      if len(journal) >= 1:
        for entry in range(len(journal)):
          print journal[entry]
      else:
        print 'Your journal is empty.'
    elif words[0] in ('quit','q'):
      exitGame()
    else:
      print 'I don\'t know what that means.'
main()