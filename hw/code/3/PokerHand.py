"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *
from array import array

class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def suit_rank(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.rank] = self.suits.get(card.rank, 0) + 1

    
    def has_pair(self):
        self.suit_rank()
        for val in self.suits.values():
            if val >= 2:
                return True
        return False
    
    def has_two_pair(self):
        self.suit_rank()
        count = 0
        for val in self.suits.values():
            if val >= 2:
                count += 1

        if count >= 2:
            return True
        return False
    
    def has_three_kind(self):
        self.suit_rank()
        count = 0
        for val in self.suits.values():
            if val >= 2:
                count += 1

        if count >= 3:
            return True
        return False
    
    def has_straight(self):
        ranks = [0] * 14
        for card in self.cards:
            if card.rank == 1:
                ranks[13] = 1
            ranks[card.rank - 1] = 1
        count = 0;
        for i in ranks:
            if i == 1:
                count += 1
                if count >= 5:
                    return True
            else:
                count = 0
        return False
        
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def has_full_house(self):
        self.suit_hist()
        three_kind = 0
        two_kind = 0
        for val in self.suits.values():
            if val >= 3:
                three_kind += 1
            elif val >= 2:
                two_kind += 1
            if three_kind > 0 and two_kind > 0:
                return True
        return False
        
    def has_four_kind(self):
        self.suit_rank()
        count = 0
        for val in self.suits.values():
            if val >= 2:
                count += 1

        if count >= 4:
            return True
        return False
        
    def has_straight_flush(self):
        str_flush = {0: [0]*14,1: [0]*14,2: [0]*14,3: [0]*14}
        for card in self.cards:
            str_flush[card.suit][card.rank] = 1
        count = 0
        for i in range(0,4):
            for j in str_flush[i]:
                if j == 1:
                    count += 1
                    if count >= 5:
                        return True
                else:
                    count = 0

        return False


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print hand.has_straight_flush()
        print ''
