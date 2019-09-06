'''Player class to record stats for individual players
'''


class Player:
    '''Player blueprint (NOT ACCURATE WHATSOEVER)

    Parameters
    ---------------------------------------------
    name : str
        Player name

    yards : int
        how many yards player ran

    touchdowns : int
        how many touchdowns player scored

    safety: int
        how many safeties player scored

    interceptions : int
        how many ducks player snagged

    field_goals : int
        how many field goals player scored
    '''
    def __init__(self, name=None, yards=120, touchdowns=5, safety=1,
                 interceptions=0, field_goals=3):
        self.name = name
        self.yards = yards
        self.touchdowns = touchdowns
        self.safety = safety
        self.interceptions = interceptions
        self.field_goals = field_goals

    def get_points(self):
        '''Gets points scored by the player from stats
        '''
        td_points = 6 * self.touchdowns['td']
        safety_points = 2 * self.safety['safety']
        fg_points = 3 * self.field_goals['fg']
        total_points = td_points + safety_points + fg_points
        return total_points


class Quarterback(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks
    '''
    def __init__(self, name=None, yards=130, touchdowns=5, completed_passes=20,
                 interceptions=4, safety=None, field_goals=None):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns,
                         safety=safety, interceptions=interceptions)
        self.completed_passes = completed_passes

    def passing_score(self):
        '''This is a random formula... FYI
        '''
        score = self.completed_passes - (2 * self.interceptions)
        return score

# TODO - refine the default player stats and/or make a defensive player default
# with number of tackles, sacks, interceptions etc.

class Defender(Player):
    '''Override certain parameters of the default player class and add some 
    functionalities unique to defense'''

    def __init__(self, name=None, tackles=10, tfl=5, sacks=3,
                 interceptions=4, safety=1, touchdowns=None):
        super().__init__(name=name, touchdowns=touchdowns,
                       safety=safety, interceptions=interceptions)

        self.tackles = tackles
        self.tfl = tfl
        self.sacks = sacks

    def defense_score(self):
        '''completely made up algorithm'''
        score = self.tackles * (self.tfl ^ self.sacks)
        return score

