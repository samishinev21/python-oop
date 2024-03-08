class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {player.guild}"
    
    def kick_player(self, player_name):
        players = []
        found = False

        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                found = True
            else:
                players.append(player)
                
        self.players = players

        if found:
            return f"Player {player.name} has been removed from the guild."
        else:
            return f"Player {player.name} is not in the guild."
        
    def guild_info(self):
        player_infos = "\n".join([player.player_info() for player in self.players])
        return f"Guild: {self.name}\n{player_infos}"