class Error(Exception):
    """Base class for exceptions in TicTacToeBoard"""
    pass

class InvalidKey(Error):
    pass


class InvalidMove(Error):
    pass


class InvalidValue(Error):
    pass


class NotYourTurn(Error):
    pass


class TicTacToeBoard:
    def __init__(self):
        self.state = {"A1": " ", "A2": " ", "A3": " ",
                      "B1": " ", "B2": " ", "B3": " ",
                      "C1": " ", "C2": " ", "C3": " "}
        self.current = "b"
        self.status = "Game in progress."

        
    def __getitem__(self, key):
        try:
            if(key[0] != "A" and
               key[0] != "B" and
               key[0] != "C" or
               key[1] != "1" and
               key[1] != "2" and
               key[1] != "3"):
                raise InvalidKey
        except InvalidKey:
            print(InvalidKey)
        else:
            return self.state[key]

        
    def __setitem__(self, key, value):
        try:
            if(key[0] != "A" and
               key[0] != "B" and
               key[0] != "C" or
               key[1] != "1" and
               key[1] != "2" and
               key[1] != "3"):
                raise InvalidKey
            elif value != "X" and value != "O":
                raise InvalidValue
            elif self.state[key] != " ":
                raise InvalidMove
            elif self.current != value:
                if self.current != "b":
                    raise NotYourTurn
        except InvalidKey:
            raise 
        except InvalidValue:
            raise
        except InvalidMove:
            raise
        except NotYourTurn:
            raise
        
        else:
            self.state[key] = value
            if self.current == "b":
                if value == "O":
                    self.current = "X"
                else:
                    self.current = "O"
            elif self.current == "X":
                self.current = "O"
            else:
                self.current = "X"

        
    def game_status(self):
        if self.status == "Game in progress.":
            self.check_end_game()
        return self.status


    def check_draw(self):
        flag = True
        for key, value in self.state:
            if self.state[key + value] == " ":
                flag = False
        return flag


    def check_end_game(self):
        cases = [["A1", "A2", "A3"], ["B1", "B2", "B3"],
                 ["C1", "C2", "C3"], ["A1", "B1", "C1"],
                 ["A2", "B2", "C2"], ["A3", "B3", "C3"],
                 ["A3", "B2", "C1"], ["A1", "B2", "C3"]]
        for case in cases:
            if (self.state[case[0]] == self.state[case[1]] and
                self.state[case[1]] == self.state[case[2]] and
                self.state[case[0]] != " " and
                self.state[case[1]] != " " and
                self.state[case[2]] != " "):
                self.status = "{0} wins!".format(self.state[case[0]])
                return self.status
        if self.check_draw():
            self.status = "Draw!"
            return self.status


    def __str__(self):
        return ("\n" +\
        "  -------------\n" +\
        "3 | {0} | {1} | {2} |\n" +\
        "  -------------\n" +\
        "2 | {3} | {4} | {5} |\n" +\
        "  -------------\n" +\
        "1 | {6} | {7} | {8} |\n" +\
        "  -------------\n" +\
        "    A   B   C  \n").format(self.state["A3"],
                                    self.state["B3"],
                                    self.state["C3"],
                                    self.state["A2"],
                                    self.state["B2"],
                                    self.state["C2"],
                                    self.state["A1"],
                                    self.state["B1"],
                                    self.state["C1"])
