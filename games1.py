#простая игра
#демонстрируем импорт модулей
import game,random
print(" добро пожаловать в игру")
again= None
while again !="n":
    players=[]
    num = game.ask_number(question = "сколько игроков участвует? (2-5)", low = 2, hight = 5)
    for i in range(num):
        name = input("имя игрока: ")
        score = random.randrange(100)+1
        player = game.Player(name, score)
        players.append(player)
        print("\n вот результат игры")
        for player in players:
            print(player)
    again = game.ask_yes_no("\n хотите сыграть еще раз(y/n)")
    input("\n\n нажмите ентре чтобы выйти")
    
                            
