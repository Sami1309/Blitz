import random


deck = ['A','A','A','A',
        '2','2','2','2',
        '3','3','3','3',
        '4','4','4','4',
        '5','5','5','5',
        '6','6','6','6',
        '7','7','7','7',
        '8','8','8','8',
        '9','9','9','9',
        '10','10','10','10','10','10','10','10','10','10','10','10','10','10',
        'BJ','BJ']



class Player:

    isMachine = True


    def __init__(self, isMachine):
        self.isMachine = isMachine

    def playTurn(self, gameEngine):



        print()
        gameEngine.showRows()
        print()
        print("Current card:", gameEngine.getDeckCard())
        print("Next card: ", gameEngine.getNextCard())
        print("Score: ", gameEngine.getScore())
        print("Streak: ",gameEngine.getStreak())
        print("Strikes: ", gameEngine.getStrikes())

        rowChoice = self.getChoice()

        gameEngine.playMove(rowChoice)

        gameEngine.takeTurn()

    def getChoice(self):
        if self.isMachine:
            return 0
        else:
            rowChosen = False
            while not rowChosen:

                row = input("Select row: ")

                rowChoice = int(row)
                if not rowChoice in [0,1,2,3]:
                    print("Please select valid row")
                else:
                    rowChosen = True
            return rowChoice



    def playGame(self, gameEngine):
        print("Playing a game of 21 Blitz")

        while not gameEngine.getIsOver():
            self.playTurn(gameEngine)
        print("Thank you for playing")



class GameEngine:

    deck = ['A','A','A','A',
        '2','2','2','2',
        '3','3','3','3',
        '4','4','4','4',
        '5','5','5','5',
        '6','6','6','6',
        '7','7','7','7',
        '8','8','8','8',
        '9','9','9','9',
        '10','10','10','10','10','10','10','10','10','10','10','10','10','10',
        'BJ','BJ']
    game_deck = []

    rows = [[],[],[],[]]
    row_vals = [[0],[0],[0],[0]]
    deck_card = ''
    next_card = ''
    score = 0
    streak = 0
    strikes = 0
    isOver = False


    def __init__(self):
        self.game_deck = self.deck[:]
        random.shuffle(self.game_deck)
        self.deck_card = self.game_deck.pop()
        self.next_card = self.game_deck[len(self.game_deck) - 1]


    def clearRow(self, row, win):
        if win:
            self.streak += 1
            if self.row_vals[row][0] == 21:
                self.score += 400
            if len(self.rows[row]) == 5:
                self.score += 600
            if self.streak >= 2:
                self.score += (self.streak - 1)*250
            if self.rows[row][-1] == 'BJ':
                self.score += 200
        else:
            self.strikes += 1
            self.streak = 0
        self.rows[row] = []
        self.row_vals[row] = [0]

    def playMove(self, row):
        
        card = self.deck_card
        if card == 'BJ':
            self.rows[row].append('BJ')
            self.row_vals[row][0] = 21
        elif card == 'A':         
            self.row_vals[row] = [self.row_vals[row][0]+1, self.row_vals[row][0]+11]  
        else:
            self.row_vals[row] = [r + int(card) for r in self.row_vals[row]]
        
        for r in self.row_vals[row]:
            if r > 21:
                self.row_vals[row].remove(r)
            if r == 21:
                self.row_vals[row][0] = 21
        
        self.rows[row].append(card)

        #if no more valid amounts for row

        if len(self.row_vals[row]) == 0:
            self.clearRow(row, False) # clear with no points, add a strike
        elif self.row_vals[row][0] == 21 or len(self.rows[row]) == 5:
            self.clearRow(row, True) # clear with points, add to streak
        else:
            self.streak = 0

        if self.strikes >= 3:
            self.gameFinish(False)

    def showRows(self):
        for i, row in enumerate(self.rows):
            print(i, ": ", row, self.row_vals[i])

    def getDeckCard(self):
        return self.deck_card

    def getNextCard(self):
        return self.next_card

    def getScore(self):
        return self.score

    def getStreak(self):
        return self.streak

    def getStrikes(self):
        return self.strikes

    def takeTurn(self):
        
        if len(self.game_deck) > 0:
            self.deck_card = self.game_deck.pop()
            if len(self.game_deck) > 0:
                self.next_card = self.game_deck[len(self.game_deck) - 1]
        else:
            self.gameFinish(True)

    def gameFinish(self,win):
        if win:
            if self.strikes == 0:
                self.score += 100
            print("Final score:")
            print(self.score)
        else:
            print("You lose")
        self.isOver = True

    def getIsOver(self):
        return self.isOver

if __name__ == '__main__':
    player1 = Player(False)

    game1 = GameEngine()

    player1.playGame(game1)


    