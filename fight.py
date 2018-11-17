import player
import monster

class Fight:
  def __init__(self,f1,f2):
    self.f1 = f1
    self.f2 = f2
  def tick(self):
    self.f1.hp=self.f1.hp-self.f2.attack()
    self.f2.hp=self.f2.hp-self.f1.attack()