# qu.py
# Alex Claman

from rooms import * # imports Room constructor
import sys          # required for quit function

room1 = Room('Living Room', 'A generic living room containing a couch,\
  a lit lamp, and a TV.',
  'couch', 'This is just a couch with a remote on it. Get over it.',
  'lamp', 'It is casting a strange shadow on the wall.', 'TV',
  'Just playing some static.',
  'An infomercial blares: Injured? Insane? We can\'t really help. Sorry.',
  'change channel')
# Letter = I
room2 = Room('Dining Room', 'There is a table and a cabinet.\
  The floor is covered by a thick carpet', 'table', 'A massive\
  oak table. On it is a single dirty fork.', 'cabinet',
  'Contains cutlery, clean utensils, and plates.', 'carpet',
  'An abnormally thick carpet. There might be something under it.', 'You\
  find a old, yellowed letter with a key inside. It reads: Everything\
  is a lie. Except the cake. It is exquisite.', 'lift carpet')
# Letter is G
room3 = Room('Parlor', 'There are several armchairs and a coffee table.',
  'armchair', 'An exceptionally comfortable leather armchair.',
  'table', 'Has some mugs and a few magazines scattered\
  atop its surface.', 'mugs', 'Sadly, they do not contain coffee.',
  'The headline reads: Avoid the tea. It\'s terrible today.','read magazine')
# Letter = T
room4 = Room('Bedroom', 'There is a bed and a wardrobe.','bed',
  'A luxurious four-poster bed with something under it. It is not yours.\
  Step away.', 'wardrobe', 'Contains a large number of old fur coats.\
  May or may not contain a portal to Narnia.', 'something',
  'A locked chest.', 'The chest contains a page reading only:\
  Bifur, Bofur, and Bombur are dwarves.','unlock chest')
# Letter = B
room5 = Room('Entry Hall','A large entry hall. Kind of dark and gloomy. \
  There\'s a coatrack, a tapestry hanging on a wall, and a chandelier.',
  'coatrack','It\'s very dusty in that corner. You cough a bit.','tapestry',
  'A very old tapestry depicting the hunt of a unicorn. It\'s probably \
  valuable.', 'chandelier','Strangely, it contains some smoking candles.',
  'You rip the tapestry down from the wall, revealing a message:\
  Do not take the oblong package. It\'s only oil.',
  'steal tapestry')
# Letter = O
room6 = Room('Guest Bedroom','A generic bedroom. It\'s not nearly as nice\
  as the other bedroom, but there\'s still a table, a chair, and a bed.',
  'table','a small table with a clock and a flashlight on it',
  'chair','Not really comfortable, but it\'ll suffice.',
  'bed','The blanket looks kind of threadbare, and the mattress is lumpy.',
  'It\'s a note reading: the Sybil is not in today. She sends her apologies.',
  'check mattress')
# Letter = S
room7 = ('Kitchen')
# Letter = D
room8 = ('Hallway')
# Letter = O
room9 = ('Laundry')
# Letter = A
room10 = ('Garden','')
# Letter = L
room11 = ('Office')
# Letter = M
room12 = ('Storage')
# Letter = I
room13 = ('Library')
# Letter = B
room14 = ('Garage')
# Letter = C
room15 = ('Art Showroom')
# Letter = U
room16 = ('Meditation Room')
# Letter = N

# winning: player has to find the recurring letter in each of the
# clues, then find the correct anagram of those letters; additionally
# player must have all items in their backpack
# The word is discombobulating

# This next block sets the connections between rooms
room1.setConnectedRoom(room4,'north','n') # room4 is north of room1
room1.setConnectedRoom(room2,'west','w')  # room2 is west of room1
room2.setConnectedRoom(room1,'east','e')  # room1 is east of room2
room2.setConnectedRoom(room3,'north','n') # room3 is north of room2
room3.setConnectedRoom(room2,'south','s') # room2 is south of room3
room3.setConnectedRoom(room4,'east','e')  # room4 is east of room3
room4.setConnectedRoom(room3,'west','w')  # room3 is west of room4
room4.setConnectedRoom(room1,'south','s') # room1 is south of room4

# room3 -- room4
#   |        |
#   |        |
# room2 -- room1

room2.setItem('key') # changes the item in room2 from None to 'key'
room4.setRequiredItem('key') # changes required_item in room4 to 'key'
room6.setItem('flashlight')
# room12.setRequiredItem('flashlight')


def playerMove(move,current_room):
  if move == 'north' or move == 'n':  # if move = north, set new_room to
    new_room = current_room.north_room # the room north of current_room
    return new_room
  elif move == 'south' or move == 's':
    new_room = current_room.south_room
    return new_room
  elif move == 'east' or move == 'e':
    new_room = current_room.east_room
    return new_room
  elif move == 'west' or move == 'w':
    new_room = current_room.west_room
    return new_room

def exitGame(): # being able to quit the game is a good idea
  sys.exit('Exiting Game...')

all_items = ['key','flashlight']

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
    if command in ('north','south','east','west','n','s','e','w'):
      if command in current_room.getExits(): #check if move direction is valid
        current_room = playerMove(command,current_room)
        info = current_room.getRoomInfo()
        print info
      else:
        print 'You can\'t move in that direction.'
    elif words[0] in ('look','l'):
      info = current_room.getRoomInfo() # get room description
      print info
    elif words[0] == 'get':
      if words[1] == current_room.item:
        backpack.append(words[1]) # adds item to backpack
        print words[1],'was added to your backpack.'
      else:
        print 'I can\'t do that.'
    elif words[0] in ('examine','ex'):
      if words[1] in current_room.listObjects():
        object_info = current_room.getObjectDescription(words[1])
        print object_info # description of object
      else:
        print 'I don\'t know what that is.'
    elif command == 'open backpack':
      if backpack != []:
        print backpack # print contents of backpack if it's not empty
      else:
        print 'Your backpack is empty.'
    elif command==current_room.getClueAction() and current_room.solved==False:
      if current_room.required_item in backpack: # if player has required item
        journal.append(current_room.clue)        # add clue to journal,
        print current_room.clue                  # print clue,
        current_room.solve()                     # set room to 'solved'.
      elif current_room.required_item == None:   # if item is not required,
        print current_room.clue                  # print clue,
        journal.append(current_room.clue)        # add clue to journal,
        current_room.solve()                     # set room to 'solved'.
      else:
        print 'I\'m sorry. I don\'t know what that means.'
    elif command==current_room.getClueAction() and current_room.solved==True:
      print 'You\'ve already found this clue.' # clues will only be shown once
      # but they're saved to the journal
    elif command == 'read journal':
      if len(journal) >= 1: # if journal is not empty
        for entry in range(len(journal)):
          print journal[entry] # display one entry per line
      else:
        print 'Your journal is empty.'
    elif words[0] in ('quit','q'):
      exitGame()
    else:
      print 'I don\'t know what that means.'
main()