

class Athlete:
    def __init__(self, first, last, age, height, pay):
        self.first = first
        self.last = last
        self.fullname = '{} {}'.format(first, last)
        self.age = age
        self.height = height
        self.pay = pay



class Player(Athlete):
    def __init__(self, first, last, age, height, pay, sport, skill):
        super().__init__(first, last, age, height, pay)
        self.sport = sport
        self.skill = skill



class Manager(Athlete):
    def __init__(self, first, last, age, height, pay, players=None):
        super().__init__(first, last, age, height, pay)
        if players is None:
            self.players = []
        else:
            self.players = players
    
    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
    
    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
    
    def print_players(self):
        for player in self.players:
            print("--->", player.fullname)


ath_1 = Athlete("Karim", "Benzema", 25, 1.82, 100000)
ath_2 = Athlete("Cristiano", "Ronaldo", 34, 1.86, 2000000)


play_1 = Player("Robert", "Levandowski", 30, 1.80, 1000000, "Football", "90")
play_2 = Player("Lionel", "Messi", 32, 1.80, 4000000, "Football", "98")


mgr_1 = Manager('Xavi', 'Hernandez', 43, 1.83, 500000, [play_1, play_2])

mgr_1.print_players()