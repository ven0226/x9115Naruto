__author__ = 'Bhashwanth'

from Card import *

class PokerHand(Hand):

    def suit_hist(self):
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            
    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if (val >= 2):
                return True
        return False
        
    def has_two_pairs(self):
        self.rank_hist()
        numofPairs = 0
        for val in self.ranks.values():
            if (val >= 2):
                numofPairs += 1
        if (numofPairs >= 2):
            return True
        else:
            return False
        
    def has_three_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if (val >= 3):
                return True
        return False
     
    def has_straight(self):
        self.rank_hist()
        straight_count = 0
        for i in range(1, 15):
            if self.ranks.get(i, 0):
                straight_count += 1
                if straight_count == 5: 
                    return True
            else:
                straight_count = 0
        return False
        
    def has_fullhouse(self):
        self.rank_hist()
        has_three_of_a_kind = False
        has_pair = False
        
        for val in self.ranks.values():
            if (val == 3):
                has_three_of_a_kind = True
            if (val == 2):
                has_pair = True
        return has_three_of_a_kind and has_pair
        
    def has_four_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if (val >= 4):
                return True
        return False
        
    def has_straight_flush(self):
        return self.has_flush() and self.has_straight()
        
    def classify(self):
        if (self.has_straight_flush()):
            return "Straight Flush"
        elif (self.has_four_of_a_kind()):
            return "Four of a kind"
        elif (self.has_fullhouse()):
            return "Fullhouse"
        elif (self.has_flush()):
            return "Flush"
        elif (self.has_straight()):
            return "Straight"
        elif (self.has_three_of_a_kind()):
            return "Three of a kind"
        elif (self.has_two_pairs()):
            return "Two pair"
        elif (self.has_pair()):
            return "Pair"
        else:
            return "Highcard"
            
hands_count = {"Highcard":0, "Pair":0, "Two pair":0, "Three of a kind":0,
        "Four of a kind":0, "Straight":0, "Flush":0, "Fullhouse":0, "Straight Flush":0}
        
if __name__ == '__main__':
    players= 5
    total_hands = 1000000
    cards_per_hand = 5
    
    for i in range(total_hands):
        deck = Deck()
        deck.shuffle()
        for i in range(players):
            hand = PokerHand()
            deck.move_cards(hand, cards_per_hand)
            hand.sort()
            hands_count[hand.classify()] += 1
    
    prob = {}
    columns = ['name','prob']
    for hand in hands_count:
        prob[hand] = hands_count[hand]/(total_hands*players*1.0)*100
    print "For " , total_hands, " iterations, Hands and their respective probablities are as given below:"
    for key in prob:
        print key, ": ", prob[key],"%"