import json

class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an active state
        self.game_active = False
        # High score should never be reset
                # High score?
        all_time_high_score = 'Chapter14_Scoring/Project_Alien_Invation_HS/high_score.json'
        with open(all_time_high_score) as f:
            high_score_json = json.load(f)
        self.high_score = int(high_score_json)



    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    