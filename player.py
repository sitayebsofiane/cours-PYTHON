class Player:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def add_score(self,new_score):
        self.score+=new_score;
        return self.score
    def getName(self):
        return self.name
    def getScore(self):
        return self.score
