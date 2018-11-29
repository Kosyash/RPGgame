class Monster: #Объявлен класс монстер
  def __init__(self,name,mtype,straight): #Конструктор класса - имя, тип, сила
    self.name=name
    self.mtype=mtype
    self.x=0
    self.y=0
    self.hp=100
    self.straight=straight
  def say(self,text): #Метод речи
    self.text=text
  def get_damage(self): #Метод вычисления наносимого урона
    self.damage=((self.straight**2)/2)*1.5
    return self.damage
  def attack(self): #Метод атаки
    return self.get_damage()/2