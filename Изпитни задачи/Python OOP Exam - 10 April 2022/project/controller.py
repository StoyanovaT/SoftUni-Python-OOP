from project.player import Player


class Controller:
    DEFAULT_PLAYERS = []
    DEFAULT_SUPPLIES = []
    SUSTENANCE_TYPES = ["Food", "Drink"]

    def __init__(self):
        self.players = self.DEFAULT_PLAYERS
        self.supplies = self.DEFAULT_SUPPLIES

    def add_player(self, *players):
        added_names = []
        for player in players:
            if player in self.players:
                continue
            self.players.append(player)
            added_names.append(player.name)
        return f"Successfully added: {', '.join(added_names)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)
        if player is None:
            return

        if sustenance_type not in self.SUSTENANCE_TYPES:
            return

        idx, supply = self.__find_supply_by_type(sustenance_type)
        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        player.stamina = min(player.stamina + supply.energy, Player.MAX_STAMINA)

        self.supplies.pop(idx)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        error_message = ''
        if first_player.stamina == 0:
            error_message += f"Player {first_player.name} does not have enough stamina."
        if second_player.stamina == 0:
            error_message += '\n' + f"Player {second_player.name} does not have enough stamina."

        if error_message:
            return error_message.strip()

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player

        first_player_damage = first_player.stamina / 2
        second_player.stamina = max(second_player.stamina - first_player_damage, 0)

        if second_player.stamina == 0:
            return f"Winner: {first_player.name}"

        second_player_damage = second_player.stamina / 2
        first_player.stamina = max(first_player.stamina - second_player_damage, 0)

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - (player.age * 2), 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = '\n'.join([str(p) for p in self.players])
        result += '\n' + '\n'.join([s.details() for s in self.supplies])
        return result

    def __find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __find_supply_by_type(self, sustenance_type):
        for idx in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[idx]
            if supply.__class__.__name__ == sustenance_type:
                return (idx, supply)
        return (-1, None)




