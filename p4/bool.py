class Machine():
    def __init__(self, name):
      self.name = name
      self.__is_on__ = False
      
    def status(self):
      status = ''
      if (self.__is_on__ == True) :
        status = 'ON'
      else : 
        status = 'OFF'
      print(self.name,'is',status)
      
    def switch_status(self):
      self.__is_on__ = not self.__is_on__
      print('! click !')
      
a = Machine('lightbulb')
a.status()
a.switch_status()
a.status()