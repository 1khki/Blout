import random

class Card:
    FACES = ['7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, face, suit):
        self._face = face
        self._suit = suit

    @property
    def face(self):
        """Return the Card's self._face value."""
        return self._face

    @property
    def suit(self):
        """Return the Card's self._suit value."""
        return self._suit

    @property
    def image_name(self):
        return str(self).replace(' ', '_') + '.png'

    def __repr__(self):
        """Return string representation for repr()."""
        return f"Card(face='{self.face}', suit='{self.suit}')"

    def __str__(self):
        """Return string representation for str()."""
        return f'{self.face} of {self.suit}'

    def __format__(self, format):
        """Return formatted string representation for str()."""
        return f'{str(self):{format}}'


class DeckOfCards:
    NUMBER_OF_CARDS = 32  # constant number of Cards for Baloot (8 faces * 4 suits)

    def __init__(self):
        """Initialize the deck."""
        self._current_card = 0
        self._deck = []

        for face in Card.FACES:
            for suit in Card.SUITS:
                self._deck.append(Card(face, suit))

    def shuffle(self):
        """Shuffle deck."""
        self._current_card = 0
        random.shuffle(self._deck)

    def deal_card(self):
        """Return one Card."""
        if self._current_card < DeckOfCards.NUMBER_OF_CARDS:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        else:
            return None

    def __str__(self):
        """Return a string representation of the current _deck."""
        s = ''
        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}'
            if (index + 1) % 4 == 0:
                s += '\n'
        return s

def explain_rules():
    """Explain the rules of Baloot."""
    rules = """
    Welcome to Baloot!
    - The game is played with 32 cards: 7, 8, 9, 10, Jack, Queen, King, and Ace of each suit (Hearts, Diamonds, Clubs, Spades).
    - The game is typically played by four players.
    - Players are dealt 5 cards each in the first round, and then 3 cards each in the second round.
    - The goal is to win as many tricks as possible.
    - The player with the highest card of the leading suit wins the trick.
    - Trump suit (الطرنيب) can be chosen, and it has higher value over other suits.
    - Points are calculated based on the number of tricks and special card combinations.
    Let's start the game!
    """
    print(rules)

def play_baloot():
    explain_rules()

    # Initialize deck and shuffle
    deck = DeckOfCards()
    deck.shuffle()

    # Deal hands to 4 players (player 1 is the user)
    players = {f'Player {i+1}': [deck.deal_card() for _ in range(8)] for i in range(4)}

    # Show the player's hand
    print("\nYour hand:")
    for i, card in enumerate(players['Player 1']):
        print(f"{i+1}: {card}")

    # Start a basic round of play (Player 1's turn)
    for _ in range(8):
        while True:
            try:
                choice = int(input("\nChoose a card to play (1-8): ")) - 1
                if 0 <= choice < len(players['Player 1']):
                    played_card = players['Player 1'].pop(choice)
                    print(f"You played: {played_card}")
                    break
                else:
                    print("Invalid choice, please choose a valid card.")
            except ValueError:
                print("Invalid input, please enter a number between 1 and 8.")

        # For simplicity, the other players will play a random card
        for i in range(2, 5):
            opponent_card = players[f'Player {i}'].pop(random.randint(0, len(players[f'Player {i}']) - 1))
            print(f"Player {i} played: {opponent_card}")

    print("\nThe round is over!")

# Start the game
play_baloot()