class Player:
  def __init__(self,name,straight):
    self.name=name
    self.straight=straight
    self.x=0
    self.y=0
    self.hp=100
  def say(self,text):
    self.text=text
  def get_damage(self):
    self.damage=((self.straight**2)/2)*1.5
    return self.damage
  def attack(self):
    return self.get_damage()/2