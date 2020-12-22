from people import public, main_person
from tools import weapon


player1 = main_person.MainPerson('John')
print(player1)
player2 = main_person.MainPerson('Kyle')
print(player2)
policeman1 = public.Policemen()
print(policeman1)
policeman1.fight(player1)
print(player1)
print(policeman1)
gun = weapon.Gun()
player2.give_item(gun)
print(player2)
mafia1 = public.Mafia()
print(mafia1)
mafia1.fight(player2)
print(player2)
print(mafia1)
