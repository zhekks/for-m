#демонстрация создания модуля
class Player(object):
    """участник игры"""
    def __init__(self, name, score = 0):
        self.name=name
        self.score=score
    def __str__(self):
        
        rep= self.name +"\t"+str(self.score)
        return rep

def ask_yes_no(question):
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response
def ask_number(question, low, hight):
    response = None
    while response not in range (low,hight):
        response =int(input(question))
    return response

    
