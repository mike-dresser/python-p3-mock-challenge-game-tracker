class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            if hasattr(self, '_title'):
                raise Exception('The game title cannot be changed!')
            else:
                self._title = title
        else:
            raise Exception('Title must be a string')
    
    def results(self):
        return [result for result in Result.all if result.game is self and isinstance(result, Result)]

    def players(self):
        all_players = [result.player for result in Result.all if result.game is self and isinstance(result, Result)]
        unique_players = []
        for player in all_players:
            if not player in unique_players:
                unique_players.append(player)
        return unique_players

    def average_score(self, player):
        all_player_scores = [result.score for result in self.results() if result.player is player]
        return sum(all_player_scores) / len(all_player_scores)


class Player:
    all = []
    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception('Username must be a string between 2 and 16 characters.')

    def results(self):
        return [result for result in Result.all if result.player is self and isinstance(result, Result)]

    def games_played(self):
        all_games = [result.game for result in Result.all if result.player is self and isinstance(result.game, Game)]
        unique_games = []
        for game in all_games:
            if not game in unique_games:
                unique_games.append(game)
        return unique_games

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        all_games_played = [result.game for result in self.results()]
        return all_games_played.count(game)
    
    def highest_scored(game):
        result = []
        for player in Player.all:
            score = game.average_score(player)
            result.append([player, score])
        return sorted(result, key= lambda score: score[1], reverse=True)[0][0]

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception()
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception()

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000:
            if hasattr(self, '_score'):
                raise Exception('The score cannot be changed!')
            else:
                self._score = score
        else:
            raise Exception('Score must be an int between 1 and 5000.')