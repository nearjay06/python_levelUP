class Person (object): 
# '''Describes a single member and all relevant attributes'''
    mammal=True
    hair_color = "Black"

    def __init__(self,y,name,height,gender):
     self.age = y
     self.name = name
     self.height = height
     self.gender = gender

    def walk (self):
      # print("{} is walking".format(self.name))
    # print(f"{self.name} is walking")
     print(self.name + " is walking")

    def eat (self,food):
        print (f"{self.name} is eating {food}")

print (Person.mammal)
print (Person.hair_color)


# print (cathy.age)
# print(cathy.height)
# print(cathy.hair_color)
# print(cathy.gender)
# cathy.walk()
# deborah.eat('Malakwang')


class Developer(Person):
 def __init__(self,language,y,name,height,gender):
     super().__init__(y,name,height,gender)
     self.language = language
 def walk (self):
  return super().walk() + 'with swag'

 def learn (self):
      print (f"{self.name} is learning {self.language}")


deborah = Developer('python',37,'kalungi',1.8,'female')
deborah.learn()



