import pandas
import print_name


class Check_Answer:
    def __init__(self):

        self.data = pandas.read_csv(
            "/Users/Cook/Documents/VS Code/Day 20/50 States Game/us-states-game-start/50_states.csv")

        self.state = self.data.state.to_list()

        self.is_right

    def is_right(self, guess):

        if guess in self.state:

            # self.row = self.data[self.data.state == guess].to_dict()

            # xcor = list(self.row["x"[0]].values())

            # ycor = list(self.row["y"[0]].values())

            self.state_data = self.data[self.data.state == guess]

            xcor = int(self.state_data.x)

            ycor = int(self.state_data.y)

            # removed list brackets at [0] to make work without list/dict
            print_name.Print_Name(guess, xcor, ycor)

            return True
        else:
            return False
