class Card():
    
    def __init__(self, suit='spades', value=1):
        # Define suit
        self.suit = suit

        # Define value
        self.value = value

    
    def __str__(self):
        # 8 of hearts
        # King of clubs
        # if self.value == 1:
        #     card_value = 'ace'
        # elif self.value == 11:
        #     card_value = 'Jack'
        # elif self.value == 12:
        #     card_value = 'Queen'
        # elif self.value == 13:
        #     card_value = 'King'
        # else:
        #     card_value = self.value
        
        # return f'{card_value} of {self.suit}'
        

        # Or build a dictionary.
        card_values = {1: 'ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
        for i in range(2, 11):
            card_values[i] = i

        return f'{card_values[self.value]} of {self.suit}'

    def __eq__(self, other):
        # True if cards have same value and suit,
        # False otherwise
        # if self.value == other.value and self.suit == other.suit:
        #     return True
        # else:
        #     return False
        return self.value == other.value and self.suit == other.suit


    def __gt__(self, other):
        # First check the suit
        if self.suit == 'hearts':
            if other.suit == 'hearts':
                return self.value > other.value
            else:
                return True
        else:
            if other.suit != 'hearts':
                return self.value > other.value
            else:
                return False


# Numpy arrays
# my_array.shape

# my_card = Card(suit='hearts', value=8)
# my_card = Card()
# print(my_card)
# print(my_card.suit)
# print(my_card.value)
# print(type(my_card))

# def f(x):
#     return x**2

# print(f)


card_1 = Card('hearts', 13)
card_2 = Card('hearts', 12)
print(card_1 > card_2)

print(card_1 < card_2)