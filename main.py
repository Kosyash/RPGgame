import player
import monster
import fight

def title_screen_selection():
  a=print('Приветствуем вас в нашей игре!')
title_screen_selection()
def get_play():
  name=input("Как твоё имя?")
  straight = int(input("Выбери силу"))

  pl = player.Player(name=name, straight=straight)
  mn = monster.Monster(name=name, mtype=0, straight=straight)

  fig = fight.Fight(pl, mn)
  fig.tick()

  print(pl.hp)
get_play()