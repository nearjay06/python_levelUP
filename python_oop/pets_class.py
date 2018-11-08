class Pets(object):
  elements = True
  items = 'mammals'

  def __init__(self,age,name):
    self.age = age
    self.name = name
  
      
animals = Pets(6,'Tom')
print("I have 3 dogs.")
print ("{} is  {}".format(animals.name,animals.age))

animals = Pets(7,'Fletcher')
print ("I have 3 dogs.")
print ("{} is  {}".format(animals.name,animals.age))

animals= Pets(9,'Fletcher')
print ("I have 3 dogs.")
print ("{} is  {}".format(animals.name,animals.age))

  
class Dogs(object):
  
  is_hungry = True

  def eat (self):
    if Dogs.is_hungry:
      print('My dog is hungry')
    else:
      print ('My dogs are not hungry.')


Dogs().eat()
    
     
























 