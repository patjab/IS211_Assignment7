import argparse
import random


'''    A die is created with variable faces and starting numbers.
       The roll function is also provided by means of a random
       generator.
'''


class Die:

    def __init__(self, faces=6, start_at=1):

        self.faces = faces
        self.startAt = start_at

    def number_of_faces(self):

        return self.faces

    def number_of_faces(self, new_number_of_faces):

        self.faces = new_number_of_faces

    def start_at(self):

        return self.startAt

    def start_at(self, new_position):

        self.startAt = new_position

    def roll(self):
        random.seed()
        return int(random.random() * self.faces) + self.startAt


'''    A player is created in order to keep score and take a turn.
       Keeping score is done by class level variables, while taking
       a turn involves the player rolling the dice and making
       decisions afterwards. Tests are done to determine if the
       player has reached the 100 points required for a win and also
       if the players' turn is finished.
'''


class Player:

    def __init__(self, identity):

        self.identity = identity
        self.score = 0
        self.tempScore = 0
        self.isWinner = False

    def identity(self):

        return self.identity

    def identity(self, new_identity):

        self.identity = new_identity

    def score(self):

        return self.score

    def score(self, new_score):

        self.score = new_score

    def is_winner(self):

        return self.isWinner

    def is_winner(self, new_result):

        self.isWinner = new_result

    # This will first roll the die and then ask if you want to hold
    # or roll again.
    def take_turn(self, the_dice):

        print "TURN FOR PLAYER %i (%i POINTS)" % (self.identity, self.score)

        while True:
            current_roll = the_dice.roll()
            self.tempScore = self.tempScore + current_roll

            print "  Die  rolled       : %i" % current_roll

            # Follow here if the player wins after rolling.
            if self.tempScore+self.score >= 100:
                print "  Points in the Hold: %i" % self.tempScore
                print "  Total points      : %i" % \
                      (self.tempScore+self.score)
                print "*****YOU ARE THE WINNER PLAYER %i*****" % self.identity
                self.isWinner = True
                break

            # Follow here if the player loses all holding points.
            if current_roll == 1:
                print "All points in the hold are lost. No score change."
                break

            print "  Points in the Hold: %i" % self.tempScore
            decision = raw_input("Type 'r' for roll and 'h' for hold. "
                                 "Decision: ")

            while decision != "r" and decision != "h":
                decision = raw_input("Error. Please only type 'r' for roll "
                                     "and 'h' for hold. Decision: ")

            # Hold will add the score to the player's total score and
            # yield turn to another player.
            if decision == "h":
                self.score += self.tempScore
                print "Your score is now %i" % self.score
                break

            # Rolling again brings one back to the top of the while loop.
            if decision == "r":
                pass

        self.tempScore = 0
        print ""


'''    A game is the interaction between the two players along with
       logic tests that determine whether the game is complete or
       shall continue onward.

'''


class Game:

    def __init__(self, num_of_players):

        self.listOfPlayers = []

        for i in range(1, num_of_players + 1):
            self.listOfPlayers.append(Player(i))

    def add_player(self, identity):

        self.listOfPlayers.append(Player(identity))

    def remove_players(self, num_to_remove = 1):

        for x in range(0, num_to_remove):
            self.listOfPlayers.pop()

    def number_of_players(self):

        return len(self.listOfPlayers)

    def start_game(self):

        die1 = Die()

        exists_no_winner = True

        # Check for a winner every turn, which will be communicated
        # through a breaks in Player(). This stops when found.
        while exists_no_winner:
            for player in self.listOfPlayers:
                player.take_turn(die1)

                if player.isWinner:
                    exists_no_winner = False
                    break

    def reset_game(self):

        for x in range(0,len(self.listOfPlayers)):
            self.listOfPlayers.pop()


'''    Main shall collect data containing the number of players that
       are participating in the game. The game will also be started
       and shall be reset when needed.

'''


def main():

    # This passes in an argument through the command prompt for the
    # number of players.
    parser = argparse.ArgumentParser()
    parser.add_argument("--numPlayers", help="Indicate how many players "
                                             "take part in the Pig Game")
    args = parser.parse_args()

    try:
        num_of_players = int(args.numPlayers)
    except ValueError:
        print "Please enter a valid value for the --numPlayers argument."
        exit()
    except TypeError:
        print "Please enter a valid value for the --numPlayers argument."
        exit()

    # This while loop allows the ability to run as many games as the user
    # wants. Starting sets up the number of players for the game while
    # resetting clears all the players.
    while True:
        if num_of_players <= 0:
            print "A game cannot exist with less than one player. Exiting."
            exit()

        game1 = Game(num_of_players)

        print "BEGINNING GAME WITH %i PLAYERS \n" % \
              game1.number_of_players()

        game1.start_game()

        print "END GAME\n"

        decision = raw_input("Do you want to play more? Type Y for another "
                             "game, all other inputs will result in"
                             " program exit. Decision: ")
        if decision != "Y":
            break

        game1.reset_game()

        while True:
            try:
                num_of_players = int(raw_input("How many players will take"
                                               " part? Answer: "))
                break
            except ValueError:
                print "Error. Try again with a valid answer."


if __name__ == "__main__":
    main()
