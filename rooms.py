# rooms.py
# code by Alex Claman

class Room():
  def __init__(self, north, east, south, west, room_name, room_desc, object_1, object_1_desc, object_2, object_2_desc, object_3, object_3_desc, clue):
    self.room_name = room_name
    self.room_desc = room_desc
    self.object_1 = object_1
    self.object_1_desc = object_1_desc
    self.object_2 = object_2
    self.object_2_desc = object_2_desc
    self.object_3 = object_3
    self.object_3_desc = object_3_desc
    self.clue = clue
    self.directions = []
    if north == True:
      self.directions.append('North')
    if east == True:
      self.directions.append('East')
    if south == True:
      self.directions.append('South')
    if west == True:
      self.directions.append('West')

  def getDirections(self):
    return self.directions

  def getRoomInfo(self):
    return self.room_name, self.room_desc

  def getObjects(self):
    return self.object_1, self.object_1_desc, self.object_2, self.object_2_desc, self.object_3, self.object_3_desc

  def getClue(self):
    return self.clue

def main():
  room1 = Room(True, 'no', 'no', True, 'Living Room', 'A generic living room', 'couch', 'This is just a couch. Get over it.', 'lamp', 'I love lamp', 'TV', 'Just playing some static', 'May all trouble begone with OxiClean.')
  print room1.getDirections()
  print room1.getRoomInfo()
  room1Objects = room1.getObjects()
  print room1Objects[0]+ ':', room1Objects[1]
  print room1Objects[2]+ ':', room1Objects[3]
  print room1Objects[4]+ ':', room1Objects[5]
  print room1.getClue()

  room2 = Room('no', True, True, True, 'Dining Room', 'There is a table and a cabinet. The floor is covered by a thick carpet.', 'table', 'A massive oak table.', 'cabinet', 'Contains cutlery, utensils, and plates.', 'carpet', 'An abnormally thick carpet. There might be something under it.', 'Everything is a lie. Except the cake.')
  print room2.getDirections()

if __name__ == "__main__":
  main()