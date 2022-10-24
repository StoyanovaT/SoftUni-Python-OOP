from project0102.horse_race import HorseRace
from project0102.horse_specification.appaloosa import Appaloosa
from project0102.horse_specification.thoroughbred import Thoroughbred
from project0102.jockey import Jockey


class HorseRaceApp:
    DEFAULT_HORSES = []
    DEFAULT_JOCKEYS = []
    DEFAULT_HORSE_RACES = []
    VALID_TYPES_HORSES = ["Appaloosa", "Thoroughbred"]
    RACE_TYPES_FREE_TO_CREATE = ["Winter", "Spring", "Autumn", "Summer"]
    MIN_PARTICIPANTS = 2

    def __init__(self):
        self.horses = self.DEFAULT_HORSES
        self.jockeys = self.DEFAULT_JOCKEYS
        self.horse_races = self.DEFAULT_HORSE_RACES

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.VALID_TYPES_HORSES:
            return

        if self.__check_if_horse_name_already_added(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
        else:
            horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.__check_if_jockey_name_exist(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type not in self.RACE_TYPES_FREE_TO_CREATE:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        self.RACE_TYPES_FREE_TO_CREATE.remove(race_type)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        if not self.__check_if_jockey_name_exist(jockey_name):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = self.__find_horse_by_type(horse_type)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        jockey = self.__find_jockey_by_name(jockey_name)

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def __check_if_horse_name_already_added(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return True
        return False

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        if not self.__check_if_horse_race_of_given_type_exist(race_type):
            raise Exception(f"Race {race_type} could not be found!")

        if not self.__check_if_jockey_name_exist(jockey_name):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        jockey = self.__find_jockey_by_name(jockey_name)

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        horse_race = self.__find_horse_race_by_type(race_type)

        if self.__check_if_jockey_already_added_to_horse_race(jockey_name, horse_race):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        if not self.__check_if_horse_race_of_given_type_exist(race_type):
            raise Exception(f"Race {race_type} could not be found!")

        horse_race = self.__find_horse_race_by_type(race_type)

        if len(horse_race.jockeys) < self.MIN_PARTICIPANTS:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        jockey_idx = 0
        horse_speed = 0

        for idx in range(len(horse_race.jockeys)):
            jockey = horse_race.jockeys[idx]
            if jockey.horse.speed > horse_speed:
                horse_speed = jockey.horse.speed
                jockey_idx = idx

        winner = horse_race.jockeys[jockey_idx]
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}" \
               f"! Winner's horse: {winner.horse.name}."

    def __check_if_jockey_name_exist(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return True
        return False

    def __find_horse_by_type(self, horse_type):
        for idx in range(len(self.horses) - 1, -1, -1):
            horse = self.horses[idx]
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse
        return None

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey_name == jockey.name:
                return jockey

    def __check_if_horse_race_of_given_type_exist(self, race_type):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                return True
        return False

    def __check_if_jockey_already_added_to_horse_race(self, jockey_name, horse_race):
        for jockey in horse_race.jockeys:
            if jockey.name == jockey_name:
                return True
        return False

    def __find_horse_race_by_type(self, race_type):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                return horse_race




