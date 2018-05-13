import random
import numpy as np


# 16.1
def rollDie():
    return random.choice([1,2,3,4,5,6])

def chackPascal(numTrials):
    """勝利する確率の評価値を表示する"""
    numWins = 0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins += 1
                break
    print('Probability of winning = ', numWins/numTrials)
    # print(numWins)
    # print(numTrials)

chackPascal(10000)


# 16.2
class CrapsGame(object):
    def __init__(self):
        self.pass_wins, self.pass_losses = 0, 0
        self.dp_wins, self.dp_losses, self.dp_pushes = 0, 0, 0

    def play_hand(self):
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.pass_wins += 1
            self.dp_losses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.pass_losses += 1
            if throw == 12:
                self.dp_pushes += 1
            else:
                self.dp_wins += 1
        else:
            point = throw
            while True:
                throw = rollDie() + rollDie()
                if throw == point:
                    self.pass_wins += 1
                    self.dp_losses += 1
                    break
                elif throw == 7:
                    self.pass_losses += 1
                    self.dp_wins += 1
                    break

    def pass_results(self):
        return (self.pass_wins, self.pass_losses)

    def dp_results(self):
        return (self.dp_wins, self.dp_losses, self.dp_pushes)



def craps_sim(hands_per_game, num_games):
    """hands_per_gameの手から成るゲームをnumGames回プレイし、
       その結果を表示する"""
    games = []

    # ゲームをnumGames回プレイする
    for t in range(num_games):
        c = CrapsGame()
        for i in range(hands_per_game):
            c.play_hand()
        games.append(c)

    # 各ゲームの統計値を求める
    pROI_per_game, dpROI_per_game = [], []
    for g in games:
        wins, losses = g.pass_results()
        pROI_per_game.append((wins - losses) / float(hands_per_game))
        wins, losses, pushes = g.dp_results()
        dpROI_per_game.append((wins - losses) / float(hands_per_game))

    # 統計値の概要を求めて表示する
    meanROI = str(round((100 * sum(pROI_per_game) / num_games), 4)) + '%'
    sigma = str(round(100 * np.std(pROI_per_game), 4)) + '%'
    print('Pass:', 'Mean ROI =', meanROI, 'Std. Dev. =', sigma)

    meanROI = str(round((100 * sum(dpROI_per_game) / num_games), 4)) + '%'
    sigma = str(round(100 * np.std(dpROI_per_game), 4)) + '%'
    print('Don\'t Pass:', 'Mean ROI =', meanROI, 'Std. Dev. =', sigma)

craps_sim(20, 10)
craps_sim(1000000, 10)
craps_sim(20, 1000000)