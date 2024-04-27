import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])  # collections로 클래스를 만든다.
# special method
## 장점
### method 이름을 외울 필요가 없다.
### standard library 효과 증가

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # [2,3,4,5,6,7,8,9,10,j,q,k,a]
    suits = 'spades diamonds clubs hearts'.split()  # [speades, diamond, clubs, hearts]

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):  # for, slicing
        return self._cards[position]


# random method 활용 
# from random import choice
# a1 = FrenchDeck()
# print(choice(a1))

# # for 활용 -> for 문을 사용할 수 있는 이유는 __getitem__ 이 존재
# a1 = FrenchDeck()
# for a in a1:
#     print(a)

# # slicing -> slicing 을 사용할 수 있는 이유는 __getitem__ 이 존재
# a1 = FrenchDeck()
# print(a1[12::13])

# # for 역순 reversed('target')
# a1 = FrenchDeck()
# for a in reversed(a1):
#     print(a)

# # FrenchDeck 클래스의 경우 반복할 수 있으므로 in 이 작동한다. __contains__ 가 없다면 in 으로 가능
# a1 = FrenchDeck()
# print(('Q', 'hearts') in a1)  # True
# print(Card('Q', 'hearts') in a1)  # True

# # 정렬
# a1 = FrenchDeck()
# for a in sorted(a1, reverse=True):
#     print(a)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
# suit_values {spades: 3, ..., clubs: 0}

def spades_high(card):
    # print(Card(card.rank, card.suit))  # rank 는 오름차순, suit 는 랜덤
    # FrenchDeck.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    rank_value = FrenchDeck.ranks.index(card.rank)  # 정렬 된 card의 rank 인덱스 위치를 rank_value에 저장 / 값 고정
    # print(card.rank) 오름차순 정렬 -> rank_value 도 오름차순 정렬
    return rank_value * len(suit_values) + suit_values[card.suit]

deck = FrenchDeck()

for card in sorted(deck, key=spades_high):  # spades_high 갖고 있는 데이터 형식에서 오름차순, key 는 어떤 값을 기준으로 정렬
    print(card)
