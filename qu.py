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
  'An abnormally thick carpet.', 'You\
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
  There\'s a coatrack, a tapestry, and a chandelier.','coatrack',
  'It\'s very dusty in that corner. You cough a bit.','chandelier',
  'Strangely, it contains some smoking candles.','tapestry','A very old \
  tapestry depicting the hunt of a unicorn.',
  'You rip the tapestry down from the wall, revealing a message that\
  fades as you read it: Do not take the oblong package. It\'s only oil.',
  'steal tapestry')
# Letter = O
room6 = Room('Guest Bedroom','A generic bedroom. It\'s not nearly as nice\
  as the other bedroom, but there\'s still a table, a chair, and a bed.',
  'table','a small table with a clock and a flashlight on it',
  'chair','Not really comfortable, but it\'ll suffice.',
  'bed','The blanket looks kind of threadbare and the mattress is sagging.',
  'It\'s a note reading: the Sybil is not in today. She sends her apologies.',
  'cut mattress')
# Letter = S
room7 = Room('Kitchen','A very well stocked and clean room with granite \
  countertops. Among other things, there\'s a French press, a dishwasher, and\
  a large oven.','press','There are still some coffee grounds in it.',
  'dishwasher','Inside are some clean plates and a knife.','oven',
  'You open the oven to find a pumpkin pie. Yum.',
  'Don\'t die here. If you do, there\'s no respawn.','eat pie')
# Letter = D
room8 = Room('Hallway','A','A','A','A','A','A','A','A','A')
# Letter = O
room9 = Room('Laundry','A','A','A','A','A','A','A','A','A')
# Letter = A
room10 = Room('Garden','A','A','A','A','A','A','A','A','A')
# Letter = L
room11 = Room('Office','A','A','A','A','A','A','A','A','A')
# Letter = M
room12 = Room('Storage','A','A','A','A','A','A','A','A','A')
# Letter = I
room13 = Room('Library','A','A','A','A','A','A','A','A','A')
# Letter = B
room14 = Room('Garage','A','A','A','A','A','A','A','A','A')
# Letter = C
room15 = Room('Art Showroom','A','A','A','A','A','A','A','A','A')
# Letter = U
room16 = Room('Meditation Room','A','A','A','A','A','A','A','A','A')
# Letter = N

# winning: player has to find the recurring letter in each of the
# clues, then find the correct anagram of those letters; additionally
# player must have all items in their backpack
# The word is discombobulating

# These blocks set the connections between rooms
# This is a corner room
room1.setConnectedRoom(room4,'north','n')
room1.setConnectedRoom(room5,'west','w')
# This is an edge room
room2.setConnectedRoom(room5,'east','e')
room2.setConnectedRoom(room7,'north','n')
room2.setConnectedRoom(room15,'west','w')
# This is a center room
room3.setConnectedRoom(room5,'south','s')
room3.setConnectedRoom(room4,'east','e')
room3.setConnectedRoom(room7,'west','w')
room3.setConnectedRoom(room8,'north','n')

room4.setConnectedRoom(room3,'west','w')
room4.setConnectedRoom(room1,'south','s')
room4.setConnectedRoom(room13,'north','n')

room5.setConnectedRoom(room1,'east','e')
room5.setConnectedRoom(room3,'north','n')
room5.setConnectedRoom(room2,'west','w')

room6.setConnectedRoom(room13,'south','s')
room6.setConnectedRoom(room11,'west','w')

room7.setConnectedRoom(room2,'south','s')
room7.setConnectedRoom(room3,'east','e')
room7.setConnectedRoom(room9,'west','w')
room7.setConnectedRoom(room12,'north','n')

room8.setConnectedRoom(room3,'south','s')
room8.setConnectedRoom(room13,'east','e')
room8.setConnectedRoom(room11,'north','n')
room8.setConnectedRoom(room12,'west','w')

room9.setConnectedRoom(room7,'east','e')
room9.setConnectedRoom(room15,'south','s')
room9.setConnectedRoom(room14,'north','n')

room10.setConnectedRoom(room12,'south','s')
room10.setConnectedRoom(room11,'east','e')
room10.setConnectedRoom(room16,'west','w')

room11.setConnectedRoom(room8,'south','s')
room11.setConnectedRoom(room6,'east','e')
room11.setConnectedRoom(room10,'west','w')

room12.setConnectedRoom(room10,'north','n')
room12.setConnectedRoom(room8,'east','e')
room12.setConnectedRoom(room7,'south','s')
room12.setConnectedRoom(room14,'west','w')

room13.setConnectedRoom(room4,'south','s')
room13.setConnectedRoom(room8,'west','w')
room13.setConnectedRoom(room6,'north','n')

room14.setConnectedRoom(room12,'east','e')
room14.setConnectedRoom(room16,'north','n')
room14.setConnectedRoom(room9,'south','s')

room15.setConnectedRoom(room2,'east','e')
room15.setConnectedRoom(room9,'north','n')

room16.setConnectedRoom(room10,'east','e')
room16.setConnectedRoom(room14,'south','s')

# Some rooms have hints
room2.hint = 'There might be something under it.'
room6.hint = 'It\'s kind of lumpy.'
room5.hint = 'It\'s hanging a bit precariously.'

room2.setItem('key') # changes the item in room2 from None to 'key'
room4.setRequiredItem('key') # changes required_item in room4 to 'key'
room6.setItem('flashlight')
room12.setRequiredItem('flashlight')
room7.setItem('knife')
room6.setRequiredItem('knife')

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
  current_room = room5
  backpack = [] # initialize backpack
  journal = []  # initialize journal
  print 'You have a journal and a backpack.'
  print 'Move using n(orth), s(outh), e(ast), and w(est).'
  print 'Interact with the environment using l(ook), ex(amine), and get.'
  print 'Explore. Investigate. Escape. And remember to check your journal.'
  while True:
    command = raw_input(">")
    words = command.split()
    if len(command) == 0:
      print 'That\'s not valid. You fool.'
    elif command in ('north','south','east','west','n','s','e','w'):
      if command in current_room.getExits(): #check if move direction is valid
        current_room = playerMove(command,current_room) # if so, move and
        info = current_room.getRoomInfo()               # print description of
        print info                                      # new room
      else:
        print 'You can\'t move in that direction.'
    elif words[0] in ('look','l') and len(command)==1: # prevents 'l <object>'
      info = current_room.getRoomInfo() # get room description
      print info
    elif words[0] == 'get':
      if current_room.solved == True: # if you've performed the clue action
        if words[1]==current_room.item and current_room.item not in backpack:
          # have typed in the correct word, and haven't found the item already
          backpack.append(words[1]) # adds item to backpack
          print words[1],'was added to your backpack.'
        else:
          # otherwise you can't find it
          print 'I can\'t do that.'
      else:
        # if you haven't performed the clue action, the item is "hidden"
        print 'I don\'t see that here.'
    elif words[0] in ('examine','ex') and len(words) == 2: # if ex has an arg
      if words[1] in current_room.listObjects(): # if object exists in room
        object_info = current_room.getObjectDescription(words[1]) # set info
        if words[1]==current_room.object_3_desc and current_room.solved==False:
          # if clue hasn't been found and object == object_3
          print object_info,current_room.hint #description of object + clue hint
        elif words[1]==current_room.object_3_desc and current_room.solved==True:
          # if clue has been found and object == object_3, just print info
          print object_info
        else:
          print object_info # prints info for the other two objects
      else:
        print 'I don\'t know what that is.'
    elif command == 'open backpack':
      if backpack != []:
        print backpack # print contents of backpack if it's not empty
      else:
        print 'Your backpack is empty.'
    elif command==current_room.getClueAction() and current_room.solved==False:
      # if clue hasn't been found
      if current_room.required_item in backpack: # if player has required item:
        journal.append(current_room.clue)        # add clue to journal,
        print current_room.clue                  # print clue,
        current_room.solve()                     # set room to 'solved'.
      elif current_room.required_item == None:   # if item is not required:
        print current_room.clue                  # print clue,
        journal.append(current_room.clue)        # add clue to journal,
        current_room.solve()                     # set room to 'solved'.
      else:
        print 'I\'m sorry. I can\'t do that.'
    elif command==current_room.getClueAction() and current_room.solved==True:
      print 'You\'ve already found this clue.' # clues will only be shown once
      # but they're automatically saved to the journal
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