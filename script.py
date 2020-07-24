class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [None for number in range(size)]
  
  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self,key, value):
    array_index = self.compress(self.hash(key))
    self.array[array_index] = [key, value]

  def retrieve(self, key)
    array_index = self.compress(self.hash(key))
    payload = self.array[array_index]
    if payload != None:
      return payload[1]
    else:
      return None
  