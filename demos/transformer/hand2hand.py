import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image as mpimg
import pydealer
from pydealer import Card

class Cards():

    def __init__(self, verbose=0):
        im = mpimg.imread('./cards.jpg')
        self.cards = im
        if (verbose):
            plt.figure(figsize=(15,15))
            plt.imshow(self.cards)
            _ = plt.axis('off')
        (self.leftmargin, self.topmargin) = (-1,1)
        (self.vspace, self.hspace) = (0,0)
        (self.height, self.width) = (178, 122)
        self.isuit = {'Clubs':0, 'Diamonds':1, 'Hearts':2, 'Spades':3}
        self.ivalue = {'Ace':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7,
                     '9':8, '10':9, 'Jack':10, 'Queen':11, 'King':12}
        k = len(self.isuit)
        self.suit = []
        for s in self.isuit:
            self.suit.append(s)
        k = len(self.ivalue)
        self.value = []
        for v in self.ivalue:
            self.value.append(v)

    def image_of_card(self, row, col):
        topleft = np.array([np.max([0,self.leftmargin + row*(self.height + self.hspace)]), \
            self.topmargin + col*(self.width + self.vspace)])
        bottomright = topleft + [self.height, self.width]
        return self.cards[topleft[0]:bottomright[0], topleft[1]:bottomright[1], :]

    def show_card(self, row, col):
        c = self.image_of_card(row, col)
        plt.figure(figsize=(2,2))
        plt.imshow(c)
        _ = plt.axis('off')
        plt.show()
        
    def show_pycard(self, card):
        s = self.isuit[card.suit]
        v = self.ivalue[card.value]
        self.show_card(s, v)
    
    def sort_cards(self, cards, ranks=pydealer.const.DEFAULT_RANKS):
        cards = sorted(cards, 
                       key=lambda x: 13*ranks["suits"][x.suit] + ranks["values"][x.value])
        return cards
        
    def sort_pyhand(self, hand):
        hand.cards = self.sort_cards(hand.cards)
        
    def is_sorted_pyhand(self, hand):
        return self.sort_cards(hand.cards) == list(hand.cards)
    
    def index_of_card(self, card):
        (s,v) = (self.isuit[card.suit], self.ivalue[card.value])
        return 13*s+v
    
    def card_of_index(self, i):
        (s,v) = (int(i/13), i%13)
        return (self.suit[s], self.value[v])
        
    def index_pyhand(self, hand):
        cards = hand.cards
        n = len(cards)
        index = np.zeros(n, dtype=int)
        for i in np.arange(len(cards)):
            index[i] = self.index_of_card(cards[i])
        return index
                        
    def show_pyhand(self, hand):
        cards = hand.cards
        n = len(cards)
        fig, axarr = plt.subplots(1, n, figsize=(1.1*n, 1.5*1))
        for i in np.arange(len(cards)):
            card = cards[i]
            s = self.isuit[card.suit]
            v = self.ivalue[card.value]
            c = self.image_of_card(s, v)
            axarr[i].imshow(c)
            axarr[i].axis('off')
        fig.tight_layout()
        plt.show()

    def show_hand(self, hand):
        n = len(hand)
        fig, axarr = plt.subplots(1, n, figsize=(1.1*n, 1.5*1))
        for i in np.arange(len(hand)):
            s, v = (int(hand[i]/13), hand[i]%13)
            c = self.image_of_card(s, v)
            axarr[i].imshow(c)
            axarr[i].axis('off')
        fig.tight_layout()
        plt.show()

    def show_ihand(hand):
        n = len(hand)
        fig, axarr = plt.subplots(1, n, figsize=(1.1*n, 1.5*1))
        for i in np.arange(len(hand)):
            s, v = (int(hand[i]/13), hand[i]%13)
            c = deck.image_of_card(s, v)
            axarr[i].imshow(c)
            axarr[i].axis('off')
        fig.tight_layout()
        plt.show()
        
        
