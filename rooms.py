# rooms.py
# code by Alex Claman

class Room():
  def __init__(self, room_name, room_desc, object_1, object_1_desc,
              object_2, object_2_desc, object_3, object_3_desc, clue, clue_action):
    self.room_name = room_name
    self.room_desc = room_desc
    self.object_1 = object_1
    self.object_1_desc = object_1_desc
    self.object_2 = object_2
    self.object_2_desc = object_2_desc
    self.object_3 = object_3
    self.object_3_desc = object_3_desc
    self.clue = clue
    self.clue_action = clue_action
    self.exits = []
    self.connectedRooms = []
    self.north_room = None
    self.south_room = None
    self.east_room = None
    self.west_room = None
    self.item = None

  def getExits(self):
    return self.exits

  def setConnectedRoom(self,room,direction):
    if direction == 'north':
      self.north_room = room
      self.connectedRooms.append(room)
      self.exits.append(direction)
    elif direction == 'south':
      self.south_room = room
      self.connectedRooms.append(room)
      self.exits.append(direction)
    elif direction == 'east':
      self.east_room = room
      self.connectedRooms.append(room)
      self.exits.append(direction)
    elif direction == 'west':
      self.west_room = room
      self.connectedRooms.append(room)
      self.exits.append(direction)

  def getConnectedRooms(self):
    return self.connectedRooms

  def getRoomInfo(self):
    return 'This is the '+ self.room_name + '. ' + self.room_desc + '.'

  def listObjects(self):
    return self.object_1, self.object_2, self.object_3

  # atwas is object in German. I'm using atwas because object is a reserved word.
  def getObjectDescription(self, atwas):
    if atwas == self.object_1:
      return self.object_1_desc
    elif atwas == self.object_2:
      return self.object_2_desc
    elif atwas == self.object_3:
      return self.object_3_desc

  def getClueAction(self):
    return self.clue_action

  def getClue(self):
    return self.clue

  def setItem(self,item):
    self.item = item

def main():
  room1 = Room(True, False, False, True, 'Living Room', 'A generic living room',
    'couch', 'This is just a couch. Get over it.', 'lamp', 'I love lamp',
    'TV', 'Just playing some static', 'May all trouble begone with OxiClean.',
    'clean couch.')
  print room1.getExits()
  print room1.getRoomInfo()
  room1Objects = room1.getObjects()
  print room1Objects[0]+ ':', room1Objects[1]
  print room1Objects[2]+ ':', room1Objects[3]
  print room1Objects[4]+ ':', room1Objects[5]
  print room1.getClue()

  room2 = Room(False, True, True, True, 'Dining Room',
    'There is a table and a cabinet. The floor is covered by a thick carpet.',
    'table', 'A massive oak table.', 'cabinet',
    'Contains cutlery, utensils, and plates.', 'carpet',
    'An abnormally thick carpet. There might be something under it.',
    'Everything is a lie. Except the cake.', 'Break GLaDOS.')
  print room2.getExits()

if __name__ == "__main__":
  main()