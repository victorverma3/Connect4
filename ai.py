#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        ''' initalizes the tiebreak strategy and the number of moves of
        lookahead.
        '''
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    def __repr__(self):
        ''' returns a string representing an AIPlayer object.
        '''
        s = 'Player '
        s += str(self.checker)
        s += ' ('
        s += self.tiebreak
        s += ', '
        s += str(self.lookahead)
        s += ')'
        return s
    def max_score_column(self, scores):
        ''' takes a list scores containing a score for each column of the board, 
            and that returns the index of the column with the maximum score.
        '''
        max_score = max(scores)
        best_scores = [x for x in range(len(scores)) if scores[x] == max_score]
        if self.tiebreak == 'LEFT':
            return best_scores[0]
        elif self.tiebreak == 'RIGHT':
            return best_scores[-1]
        else:
            rand_index = random.randint(0, len(best_scores) - 1)
            return best_scores[rand_index]
    def scores_for(self, b):
        ''' takes a Board object b and determines the called AIPlayer‘s scores for 
            the columns in b.
        '''
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == -1:
                    scores[col] = -1
                else:
                    scores[col] = 50
                b.remove_checker(col)
        return scores
    def next_move(self, b):
        ''' return the called AIPlayer‘s judgment of its best possible move.
        '''
        move = self.max_score_column(self.scores_for(b))
        self.num_moves +=1
        return move