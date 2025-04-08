class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, name, position):
        player = self.Player(name, position, self)
        self.players.append(player)

    def get_info(self):
        print(f"Team Name: {self.team_name}")
        for player in self.players:
            player.display_player_info()

    class Player:
        def __init__(self, name, position, team):
            self.name = name
            self.position = position
            self.team = team

        def display_player_info(self):
            print(f"Name: {self.name} | position: {self.position} | team: {self.team.team_name}")

team_a = Team("Barcelona")
team_a.add_player("taruna", "striker")
team_a.add_player("wahyudi", "kiper")

team_a.get_info()








