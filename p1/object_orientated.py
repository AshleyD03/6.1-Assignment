class person :
  def __init__(self, name) :
    self.name = name 
    self.friends = []
    
  def friend_list(self) :
    print(self.name + "'s friends are :")
    for i in range (len(self.friends)) :
      f = self.friends[i]
      print(str(i + 1) + ' - ' + f.name)
    
p1 = person('ashley')
p2 = person('craig')

p1.friends.append(p2)
p1.friend_list()