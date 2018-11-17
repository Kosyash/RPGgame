class Monster:
  def __init__(self,name,mtype,straight):
    self.name=name
    self.mtype=mtype
    self.x=0
    self.y=0
    self.hp=100
    self.straight=straight
  def say(self,text):
    self.text=text
  def get_damage(self):
    self.damage=((self.straight**2)/2)*1.5
    return self.damage
  def attack(self):
    return self.get_damage()/2