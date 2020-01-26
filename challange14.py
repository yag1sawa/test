from random import shuffle

class Card:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9",
              "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(0, 4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("プレーヤー１の名前を入れてください：")
        name2 = input("プレーヤー２の名前を入れてください：")
        self.deck = Deck()
        self.p1 = Player(name1) #self.p1は、Playerクラスのインスタンス(属性を３つもつ)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "このラウンドは {} が勝ちました。"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = " {} は {} 、 {} は {} を引きました。"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        #self.deckはDockクラスのインスタンス(=オブジェクト=Dock()である)。そのインスタンス変数を呼び出すメソッドが.cards。
        #Dockクラスによってインスタンスが作成され、インスタンス変数が呼び出されて左辺のcardsに代入された。
        print("バトルを始めます")
        while len(cards) >= 2:
            m = "qで終了、それ以外のキーでplay:"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print("ゲーム終了！ {} の勝ちです！".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け"

game = Game()
game.play_game()