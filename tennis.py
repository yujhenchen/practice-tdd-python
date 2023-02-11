class Tennis:
    def __init__(self, player1, player2) -> None:
        self.__player1 = player1
        self.__player2 = player2
        self.playerMap = {self.__player1: 0, self.__player2: 0}
        self.scoreMap = {0: "love", 1: "fifteen", 2: "thrity", 3: "forty", 4: "win"}
        return

    def score(self) -> None:
        self.scoreCal()
        print(
            "{player1} {player2}".format(
                player1=self.scoreMap[self.playerMap[self.__player1]],
                player2=self.scoreMap[self.playerMap[self.__player2]],
            )
        )

    def scoreCal(self) -> list:
        # do some calculation
        # if both score the same
        #   if any < 3
        #   else
        player1Score = self.playerMap[self.__player1]
        player2Score = self.playerMap[self.__player2]
        if self.playerMap[self.__player1] == self.playerMap[self.__player2]:
            if player1Score >= 3 or player2Score >= 3:
                return ["duce"]
        return []

    def clickButton1(self) -> None:
        self.playerMap[self.__player1] = self.playerMap[self.__player1] + 1
        self.score()

    def clickButton2(self) -> None:
        self.playerMap[self.__player2] = self.playerMap[self.__player2] + 1
        self.score()


if __name__ == "__main__":
    tennis = Tennis("Amy", "Tom")
    tennis.score()
