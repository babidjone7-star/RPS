import random

game = ["камень" , "ножницы" , "бумага"]
PlayerScore = 0
BotScore = 0
IsGameTrue = True

class User:
    def __init__(self):
        print("Lets Start Game!")
    def mainer(UesOrNo):
      
        global PlayerScore
        global BotScore
                  
        print(f"Ну привет  , начнешь игру?(0- да, 1 - нет) Твой счет: {PlayerScore} , Счет бота: {BotScore}")
        UesOrNo = int(input())
        if UesOrNo == 0:
          
          YourNumber = input("Выбери камень, ножницы или бумага, твой ответ: ").lower().strip()
          BotNumber = ""
          
          BotNumber = random.choice(game)

          if BotNumber == YourNumber:
            print(f"Я выбрал: {BotNumber} , у нас ничья")
            PlayerScore += 1
            BotScore += 1

          elif (YourNumber == "камень" and BotNumber == "ножницы") or \
             (YourNumber == "ножницы" and BotNumber == "бумага") or \
             (YourNumber == "бумага" and BotNumber == "камень"):
            print("Вы победили!")
            PlayerScore += 1
            
          else:
            print("Вы проиграли!")
            BotScore += 1

        if PlayerScore == 3:
           print(f"Ты победил!! счет бота: {BotScore}")
           PlayerScore = 0
           BotScore = 0

        if BotScore == 3:
           print(f"Ты проиграл!! твой счет : {PlayerScore}")
           PlayerScore = 0
           BotScore = 0

        if UesOrNo == 1:
           print("Очень жалко!")
        random.shuffle(game)
user = User()
print(user.mainer())
#print(user.Proverka())

random.shuffle(game)

while True:
     print(user.mainer())