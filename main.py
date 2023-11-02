import random

ALIGNMENTS = ["Good", "Neutral", "Evil"]

CLASS_ALIGNMENTS = {
    "Priest": ["Good", "Evil"],
    "Thief": ["Neutral", "Evil"],
    "Ninja": ["Evil"],
    "Lord": ["Good"],
}

RACES = [
    "Human",
    "Elf",
    "Dwarf",
    "Gnome",
    "Hobbit",
    "Faerie",
    "Lizard Man",
    "Draconian",
    "Rawulf",
    "Mook",
    "Felpurr",
]

CLASSES = ["Fighter", "Mage", "Thief", "Cleric"]

SEXES = ["male", "female"]

STATS = {
    "ST": {
        "name": "Strength",
        "description": "Increases physical damage done and the hit rate for\
                all physical attacks.",
    },
    "AG": {
        "name": "Agility",
        "description": "Increases chance to disarm attacks, flee, and dodge.\
                Also increases a character's ability to disarm traps without\
                misfire.",
    },
    "VT": {
        "name": "Vitality",
        "description": "Increases the amount of hit points a character\
                receives when they level up.",
    },
    "IQ": {
        "name": "Intelligence",
        "description": "Increases the effectiveness and success rate of\
                mage/psionic spells.",
    },
    "PI": {
        "name": "Piety",
        "description": "Increases the effectiveness and success rate for all\
                priest spells.",
    },
    "LK": {
        "name": "Luck",
        "description": "Increases your resistance to status effects and chance\
                for rare items to drop from enemies. Also increases ability to\
                disarm traps without misfire.",
    },
}

BASE_STATS = {
    "Human": {"ST": 9, "IQ": 8, "PI": 8, "VT": 9, "AG": 8, "LK": 8},
    "Elf": {"ST": 7, "IQ": 10, "PI": 10, "VT": 7, "AG": 9, "LK": 8},
    "Dwarf": {"ST": 11, "IQ": 6, "PI": 10, "VT": 12, "AG": 7, "LK": 7},
    "Gnome": {"ST": 10, "IQ": 7, "PI": 13, "VT": 10, "AG": 6, "LK": 7},
    "Hobbit": {"ST": 8, "IQ": 7, "PI": 6, "VT": 9, "AG": 10, "LK": 11},
    "Faerie": {"ST": 5, "IQ": 11, "PI": 6, "VT": 6, "AG": 14, "LK": 11},
    "Lizard Man": {"ST": 12, "IQ": 5, "PI": 5, "VT": 14, "AG": 9, "LK": 7},
    "Draconian": {"ST": 10, "IQ": 7, "PI": 6, "VT": 12, "AG": 8, "LK": 8},
    "Rawulf": {"ST": 8, "IQ": 6, "PI": 12, "VT": 10, "AG": 8, "LK": 9},
    "Mook": {"ST": 10, "IQ": 10, "PI": 6, "VT": 10, "AG": 7, "LK": 8},
    "Felpurr": {"ST": 7, "IQ": 10, "PI": 7, "VT": 7, "AG": 12, "LK": 10},
}

MAX_STATS = {
    "Human": {"ST": 19, "IQ": 18, "PI": 18, "VT": 19, "AG": 18, "LK": 18},
    "Elf": {"ST": 17, "IQ": 20, "PI": 20, "VT": 17, "AG": 19, "LK": 18},
    "Dwarf": {"ST": 21, "IQ": 16, "PI": 20, "VT": 22, "AG": 17, "LK": 17},
    "Gnome": {"ST": 20, "IQ": 17, "PI": 23, "VT": 20, "AG": 16, "LK": 17},
    "Hobbit": {"ST": 18, "IQ": 17, "PI": 16, "VT": 19, "AG": 20, "LK": 21},
    "Faerie": {"ST": 15, "IQ": 21, "PI": 16, "VT": 16, "AG": 24, "LK": 21},
    "Lizard Man": {"ST": 22, "IQ": 15, "PI": 15, "VT": 24, "AG": 19, "LK": 17},
    "Draconian": {"ST": 20, "IQ": 17, "PI": 16, "VT": 22, "AG": 18, "LK": 18},
    "Rawulf": {"ST": 18, "IQ": 16, "PI": 22, "VT": 20, "AG": 18, "LK": 19},
    "Mook": {"ST": 20, "IQ": 20, "PI": 16, "VT": 20, "AG": 17, "LK": 18},
    "Felpurr": {"ST": 17, "IQ": 20, "PI": 17, "VT": 17, "AG": 22, "LK": 20},
}

SEX_BONUSES = {
    "male": {"ST": 1},
    "female": {"VT": 1},
}


class Character:
    def __init__(
        self,
        name="Nobody",
    ):
        self.name = name
        self.race = self.select_race()
        self.sex = self.select_sex()
        # self.statistics = self.set_statstics()

    def select_race(self):
        race_list = ", ".join(RACES).lower()
        race = input(
            f"Please select a race for {self.name}: "
            f"{race_list}\n"
            f"Race: "
        ).lower()
        while race not in race_list:
            raise ValueError(
                f"Invalid race: {race}. Must be one of: "
                f"{', '.join(race_list)}"
            )
            self.select_race()
        return race

    def select_sex(self):
        sex_list = ", ".join(SEXES)
        sex = input(
            f"Please select a sex for {self.name}: " f"{sex_list}\n" f"Sex: "
        ).lower()
        while sex not in sex_list:
            raise ValueError(
                f"Invalid sex: {sex}. Must be one of: "
                f"{', '.join(sex_list)}"
            )
        return sex

    def set_statstics(self):
        base_stats = BASE_STATS[self.race]
        self.strength = base_stats["ST"]
        self.agility = base_stats["AG"]
        self.vitality = base_stats["VT"]
        self.intelligence = base_stats["IQ"]
        self.piety = base_stats["PI"]
        self.luck = base_stats["LK"]

        # generate a random number of bonus points, and prompt the user for the stat they want to add a point to. Add a point to the character's stat and subtract a point from the bonus point pool Keep doing this until all bonus points are expended.
        self.bonus_points = random.randint(5, 21)

        print(self)

        # while self.bonus_points > 0:
        #     stat = random.choice(["STR", "INT", "PIE", "VIT", "AGI", "LUC"])
        #     if character["Stats"][stat] < 18:  # assuming max stat value is 18
        #         character["Stats"][stat] += 1
        #         bonus_points -= 1
        # return character

    # def select_class(self):
    #     class_list = ", ".join(CLASSES)
    #     self.character_class = input(
    #         f"Please select a class for {self.name}: "
    #         f"{class_list}\n"
    #         f"Class: "
    #     )


bob = Character("Bob")

print(bob.__str__())
>>>>>>> Stashed changes
